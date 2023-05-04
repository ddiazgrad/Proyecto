fs = 8000; % frecuencia de muestreo
t = (0:1/fs:1).'; % vector de tiempo
f1 = 10;
x1 = cos(2*pi*t*f1);

fc = 1091e6;
c = physconst('LightSpeed');
lam = c/fc;
fsig = 5.8e9;

% antenna = phased.IsotropicAntennaElement( ...
%     'FrequencyRange',[800e6 6e9]);
% N = 7;
% theta = 360/N;
% thetarad = deg2rad(theta);
% 
% arclength = 0.09;
% radius = arclength/thetarad;
% 
% ang = (0:N-1)*theta;
% ang(ang >= 180.0) = ang(ang >= 180.0) - 360.0;
% 
% % Aplicar variación a la posición de los elementos
% variacion = 0.5; % Puedes ajustar este valor para cambiar la variación
% radius_variado = radius + radius * variacion * (rand(1, N) - 0.5);
% ang_variado = ang + variacion * (rand(1, N) - 0.5) * theta;
% ang_variado = wrapTo180(ang_variado); % Asegurarse de que los ángulos estén dentro del rango [-180, 180]
% 
% array = phased.ConformalArray;
% array.ElementPosition = [radius_variado.*cosd(ang_variado);...
%     radius_variado.*sind(ang_variado);...
%     zeros(1,N)];
% array.ElementNormal = [ang_variado;zeros(1,N)];


% viewArray(array,'ShowNormals',true)
% Vector de ángulos para el barrido
angles = -175:1:175;
num_runs = 100;
% Vector para almacenar las diferencias entre el ángulo real y el estimado
angle_diff = zeros(length(angles), num_runs);

estimator = phased.BeamscanEstimator2D('SensorArray',array,...
    'OperatingFrequency',fsig,...
    'DOAOutputPort',true,'AzimuthScanAngles',-180:0.001:180);


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