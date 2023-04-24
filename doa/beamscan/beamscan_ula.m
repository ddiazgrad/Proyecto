f1 = 1091e6;
f2 = 5.8e9;
doa1 = [-37;0];
doa2 = [40;20];
fc = 150e6;
c = physconst('LightSpeed');
lam = c/fc;
fs = 8000;
antenna = phased.IsotropicAntennaElement( ...
    'FrequencyRange',[800e6 6e9]);
N = 7;

array = phased.ULA('NumElements',N,'ElementSpacing',lam*0.5,...
    'Element',antenna);% t = (0:1/fs:1).';
% Calcular el número de puntos de muestreo
num_muestras = round(1 * fs);

% Generar el vector de tiempo
t = linspace(0, 1, num_muestras).';

x1 = cos(2*pi*t*f1);
x2 = cos(2*pi*t*f2);
x = collectPlaneWave(array,[x1 x2],[doa1,doa2],fc);
noise = 0.1*(randn(size(x))+1i*randn(size(x)));

estimator = phased.BeamscanEstimator2D('SensorArray',array,...
    'OperatingFrequency',fc,...
    'DOAOutputPort',true,...
    'NumSignals',2);
[~,doas] = estimator(x + noise);

plotSpectrum(estimator);
