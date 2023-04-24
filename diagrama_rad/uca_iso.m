az = -180:180;
el = 0;
fc = 1091e6;
f = [1091e6 2.4e9 5.8e9];
antenna = phased.IsotropicAntennaElement( ...
    'FrequencyRange',[800e6 6e9]);
N = 7;
theta = 360/N;
thetarad = deg2rad(theta);

arclength = 0.5*(physconst('LightSpeed')/fc);
radius = arclength/thetarad;

ang = (0:N-1)*theta;
ang(ang >= 180.0) = ang(ang >= 180.0) - 360.0;

array = phased.ConformalArray;
array.ElementPosition = [radius.*cosd(ang);...
    radius.*sind(ang);...
    zeros(1,N)];
array.ElementNormal = [ang;zeros(1,N)];
figure(3)
viewArray(array,'ShowNormals',true)
view(0,90)
figure(2)
pattern(array,f,az,el,'CoordinateSystem','polar','Type','powerdb',...
    'Normalize',true,'PropagationSpeed',physconst('LightSpeed'))
