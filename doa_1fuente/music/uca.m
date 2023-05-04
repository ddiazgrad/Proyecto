fs = 8000; % frecuencia de muestreo
t = (0:1/fs:1).'; % vector de tiempo
f1 = 10;
x1 = cos(2*pi*t*f1);

fc = 1091e6;
c = physconst('LightSpeed');
lam = c/fc;
fsig = 1091e6;

antenna = phased.IsotropicAntennaElement( ...
    'FrequencyRange',[800e6 10e9]);
N = 7;
theta = 360/N;
thetarad = deg2rad(theta);

arclength = 0.09;
radius = arclength/thetarad;

ang = (0:N-1)*theta;
ang(ang >= 180.0) = ang(ang >= 180.0) - 360.0;

array = phased.ConformalArray('Element',antenna);
array.ElementPosition = [radius.*cosd(ang);...    
radius.*sind(ang);...   
zeros(1,N)];
array.ElementNormal = [ang;zeros(1,N)];


% viewArray(array,'ShowNormals',true)
% Vector de ángulos para el barrido
angles = -175:1:175;
num_runs = 100;
% Vector para almacenar las diferencias entre el ángulo real y el estimado
angle_diff = zeros(length(angles), num_runs);


estimator = phased.MUSICEstimator2D('SensorArray',array,...
    'OperatingFrequency',fsig,...
    'NumSignalsSource','Property',...
    'DOAOutputPort',true,...
    'AzimuthScanAngles',-180:0.001:180);


SNR_dB = 10;
% Calcular la potencia de la señal de interés
Ps = norm(x1)^2;
% Calcular la potencia del ruido
SNR = 10^(10/10); % Relación señal a ruido de 10 dB
Pn = Ps/SNR;

% Vector para almacenar el valor máximo de la diferencia para cada ángulo
max_diff = zeros(length(angles), 1);
rmse_angles = zeros(length(angles), 1);
for i = 1:length(angles)
    disp(i)
    % Actualizar el valor del azimuth de doa1 en cada iteración
    doa1(1) = angles(i);
    
    for j = 1:num_runs
        % Generar la señal recibida con el nuevo valor de doa1
        x = collectPlaneWave(array,x1,doa1,fsig);

        % Generar el ruido con la potencia ajustada
        noise = sqrt(Ps/Pn)*(randn(size(x))+1i*randn(size(x)));

        % Estimar el ángulo con MVDREstimator2D
        [~,doas] = estimator(x + noise);


        % Almacenar la diferencia entre el ángulo real y el estimado
        angle_diff(i, j) = doas(1) - doa1(1);
    end
    disp(['DOA estimada para i = ' num2str(i) ' real: ' num2str(doa1(1)) ' estimado: ' num2str(doas(1))]);
    % Calcular la RMSE para el ángulo actual
    rmse_angles(i) = sqrt(mean(angle_diff(i,:).^2));
     % Almacenar el valor máximo de la diferencia para este ángulo
    max_diff(i) = max(abs(angle_diff(i,:)));
end
% Graficar las diferencias
figure(1);
plot(angles, mean(angle_diff, 2));
xlabel('Azimuth');
ylabel('Diferencia de ángulo estimado (grados)');% Graficar las RMSE para cada ángulo

figure(2);
plot(angles, rmse_angles);
xlabel('Azimuth');
ylabel('RMSE');

% Graficar el valor máximo de la diferencia para cada ángulo
figure(3);
plot(angles, max_diff);
xlabel('Azimuth');
ylabel('Máxima diferencia de ángulo estimado (grados)');