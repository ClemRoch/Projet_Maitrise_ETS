

function sarImage = reconstructSAR(sarData,matchedFilter,xStepM,yStepM,xySizeT)

[yPointM,xPointM] = size(sarData);
[yPointF,xPointF] = size(matchedFilter);


if (xPointF > xPointM)
    sarData = padarray(sarData,[0 floor((xPointF-xPointM)/2)],0,'pre');
    sarData = padarray(sarData,[0 ceil((xPointF-xPointM)/2)],0,'post');
else  
    matchedFilter = padarray(matchedFilter,[0 floor((xPointM-xPointF)/2)],0,'pre');
    matchedFilter = padarray(matchedFilter,[0 ceil((xPointM-xPointF)/2)],0,'post');
end

if (yPointF > yPointM)
    sarData = padarray(sarData,[floor((yPointF-yPointM)/2) 0],0,'pre');
    sarData = padarray(sarData,[ceil((yPointF-yPointM)/2) 0],0,'post');
else  
    matchedFilter = padarray(matchedFilter,[floor((yPointM-yPointF)/2) 0],0,'pre');
    matchedFilter = padarray(matchedFilter,[ceil((yPointM-yPointF)/2) 0],0,'post');
end

%% IMAGE SAR
sarDataFFT = fft2(sarData);
matchedFilterFFT = fft2(matchedFilter);
sarImage = fftshift(ifft2(sarDataFFT .* matchedFilterFFT));

%% Definitions des axes
[yPointT,xPointT] = size(sarImage);

xRangeT = xStepM * (-(xPointT-1)/2 : (xPointT-1)/2); 
yRangeT = yStepM * (-(yPointT-1)/2 : (yPointT-1)/2); 

%% Reduction de la taille de l'image
indXpartT = xRangeT>(-xySizeT/2) & xRangeT<(xySizeT/2);
indYpartT = yRangeT>(-xySizeT/2) & yRangeT<(xySizeT/2);

xRangeT = xRangeT(indXpartT);
yRangeT = yRangeT(indYpartT);
sarImage = sarImage(indYpartT,indXpartT);


%% Afficher
figure; mesh(xRangeT,yRangeT,abs(fliplr(sarImage)),'FaceColor','interp','LineStyle','none')
view(2)
colormap('jet');

xlabel('Horizontal (mm)')
ylabel('Vertical (mm)')
titleFigure = "SAR Image - Matched Filter Response";
title(titleFigure)


