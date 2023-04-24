f1 = 1091e6;
f2 = 1091e6;
doa1 = [-37;0];
doa2 = [40;20];
fc = 1091e6;
c = physconst('LightSpeed');
lam = c/fc;
fs = 8000;


antenna = phased.IsotropicAntennaElement( ...
    'FrequencyRange',[800e6 6e9]);
N = 7;
array = phased.ULA('NumElements',N,'ElementSpacing',lam/2,...
    'Element',antenna);
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