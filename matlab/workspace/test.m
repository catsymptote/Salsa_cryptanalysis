% Example from mathworks.com:
% https://se.mathworks.com/help/images/image-processing-operator-approximation-using-deep-learning.html

%% Imports
% for the bilateralFilterDataset function.
%import imbilatfilt
%import imwrite


%% Download Training and Test Data
%imagesDir = tempdir;
imagesDir = 'D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\models'
url_1 = 'http://www-i6.informatik.rwth-aachen.de/imageclef/resources/iaprtc12.tgz';
%downloadIAPRTC12Data(url_1,imagesDir);

trainImagesDir = fullfile(imagesDir,'iaprtc12','images','39');
exts = {'.jpg','.bmp','.png'};
pristineImages = imageDatastore(trainImagesDir,'FileExtensions',exts);

% Write out 
numel(pristineImages.Files)


%% Prepare Training Data
preprocessDataDir = [trainImagesDir filesep 'preprocessedDataset'];
%bilateralFilterDataset(pristineImages,preprocessDataDir);
%bilatFilteredImages = imageDatastore(preprocessDataDir,'FileExtensions',exts);
