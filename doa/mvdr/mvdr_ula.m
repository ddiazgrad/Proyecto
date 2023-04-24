fs = 8000;

% Calcular el número de puntos de muestreo
num_muestras = round(1 * fs);

% Generar el vector de tiempo
t = linspace(0, 1, num_muestras).';

x1 = cos(2*pi*t*1091e6);
x2 = cos(2*pi*t*5.8e9);

fc = 1091e6;
c = physconst('LightSpeed');
lam = c/fc;

antenna = phased.IsotropicAntennaElement( ...
    'FrequencyRange',[800e6 6e9]);
N = 7;

array = phased.ULA('NumElements',N,'ElementSpacing',lam*0.5,...
    'Element',antenna);


x = collectPlaneWave(array,[x1 x2],[-37 0;40 20]',fc);

noise = 0.1*(randn(size(x))+1i*randn(size(x)));

estimator = phased.MVDREstimator2D('SensorArray',array,...
    'OperatingFrequency',fc,...
    'DOAOutputPort',true,'NumSignals',2,...
    'AzimuthScanAngles',-50:50);
[~,doas] = estimator(x + noise);

plotSpectrum(estimator)