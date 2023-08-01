

function matchedFilter = createMatchedFilter(xPointM,xStepM,yPointM,yStepM,zTarget)

f0 = 77e9; % start frequency
c = physconst('lightspeed');


x = xStepM * (-(xPointM-1)/2 : (xPointM-1)/2) * 1e-3; % xStepM is in mm
y = (yStepM * (-(yPointM-1)/2 : (yPointM-1)/2) * 1e-3).'; % yStepM is in mm
      

z0 = zTarget*1e-3; % zTarget is in mm


k = 2*pi*f0/c;
matchedFilter = exp(-1i*2*k*sqrt(x.^2 + y.^2 + z0^2));