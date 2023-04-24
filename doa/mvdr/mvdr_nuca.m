fs = 8000;

% Calcular el número de puntos de muestreo
num_muestras = round(1 * fs);

% Generar el vector de tiempo
t = linspace(0, 1, num_muestras).';

x1 = cos(2*pi*t*1091e6);
x2 = cos(2*pi*t*1091e6);

fc = 1091e6;

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

x = collectPlaneWave(array,[x1 x2],[-37 0;40 20]',fc);

noise = 0.1*(randn(size(x))+1i*randn(size(x)));

estimator = phased.MVDREstimator2D('SensorArray',array,...
    'OperatingFrequency',fc,...
    'DOAOutputPort',true,'NumSignals',2,...
    'AzimuthScanAngles',-50:50);
[~,doas] = estimator(x + noise);

plotSpectrum(estimator)