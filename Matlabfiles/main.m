
%% Load les datas
dataName = 'rawData3D_simple2D';
rawData = load(dataName);
rawData = rawData.(dataName);

%% constantes
c = physconst('lightspeed');
fS = 9121e3;        % Sampling rate (sps)
Ts = 1/fS;          
K = 63.343e12;      % Slope const (Hz/sec)

%% Parametres
nFFT1d = 1024;    % FFT1D nb de points
z0 = 280e-3;        % Portee de la cible
dx = 200/406;       % Distance d'echantillonage en x
dy = 2;             % """" en y
nFFTspace = 1024;   % FFT2D nb de points


rawDataFFT = fft(rawData,nFFT1d);

tI = 4.5225e-10;
k = round(K*Ts*(2*z0/c+tI)*nFFT1d); 
sarData = squeeze(rawDataFFT(k+1,:,:));

%% Graph densite

% Convertir les vecteurs en matrices pour la fonction surf
[X, Y] = meshgrid(1:size(sarData, 2), 1:size(sarData, 1));

Z = abs(sarData);

% Tracer la surface 3D
figure;
surf(X, Y, Z);

% Ajouter l'éclairage
lighting gouraud;
camlight;

% Modifier le shading
shading interp;

xlabel('Channel');
ylabel('Peak Index');
zlabel('Peak Intensity');
title('Peak Intensity for each channel');

%% Matched Filter
matchedFilter = createMatchedFilter(nFFTspace,dx,nFFTspace,dy,z0*1e3);

%% Reconstruction Image
imSize = 200; % Size of image area in mm
sarImage = reconstructSAR(sarData,matchedFilter,dx,dy,imSize);