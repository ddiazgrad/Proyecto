f1 = 1091e6;
f2 = 2.4e9;
doa1 = [-37;0];
doa2 = [40;20];
fc = 150e6;
c = physconst('LightSpeed');
lam = c/fc;
fs = 8000;


N = 7;
theta = 360/N;
thetarad = deg2rad(theta);

arclength = 0.5*(physconst('LightSpeed')/fc);
radius = arclength/thetarad;

ang = (0:N-1)*theta;
ang(ang >= 180.0) = ang(ang >= 180.0) - 360.0;

% Aplicar variación a la posición de los elementos
variacion = 0.5; % Puedes ajustar este valor para cambiar la variación
radius_variado = radius + radius * variacion * (rand(1, N) - 0.5);
ang_variado = ang + variacion * (rand(1, N) - 0.5) * theta;
ang_variado = wrapTo180(ang_variado); % Asegurarse de que los ángulos estén dentro del rango [-180, 180]

array = phased.ConformalArray;
array.ElementPosition = [radius_variado.*cosd(ang_variado);...
    radius_variado.*sind(ang_variado);...
    zeros(1,N)];
array.ElementNormal = [ang_variado;zeros(1,N)];

% t = (0:1/fs:1).';
% Calcular el número de puntos de muestreo
num_muestras = round(1 * fs);

% Generar el vector de tiempo
t = linspace(0, 1, num_muestras).';

x1 = cos(2*pi*t*f1);
x2 = cos(2*pi*t*f2);
x = collectPlaneWave(array,[x1 x2],[doa1,doa2],fc);
noise = 0.1*(randn(size(x))+1i*randn(size(x)));


estimator = phased.MUSICEstimator2D('SensorArray',array,...
    'OperatingFrequency',fc,...
    'NumSignalsSource','Property',...
    'DOAOutputPort',true,'NumSignals',2,...
    'AzimuthScanAngles',-50:.5:50);
[~,doas] = estimator(x + noise)


plotSpectrum(estimator);