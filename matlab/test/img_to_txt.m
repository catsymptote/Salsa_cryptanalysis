clc
clear

images = dir('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\PT_img\*.jpg');


for i=1%:length(images)
    % Get file names and paths.
    file_name = images(i).name;
    read_path = fullfile('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\PT_img\', file_name);
    write_path= fullfile('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\PT_txt\', [file_name(1:end-4) '.txt']);
    disp(file_name);
    disp(read_path);
    disp(write_path);
    
    % Read files.
    %image_data = imread('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\test_image2.jpg');
    image_data = imread(read_path);
    image_data = imresize(image_data, [256 256]);
    image_data = image_data(:,:,1);
    image_data = image_data(:);

    for idx = 1:length(image_data)
        converted_text(idx) = unicode2native(char(image_data(idx)));
    end

    %reshape image_data = imreshape(image_data, [256 256]); imwrite
    %converted_text = reshape(converted_text, [256 256]);

    % Write files.
    %fileID = fopen('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\test_image2.txt','w');
    fileID = fopen(write_path,'w');
    fwrite(fileID, converted_text, 'uint8');
    fclose(fileID);
    
    dlmwrite('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\PT_txt\test.txt',converted_text,'delimiter',' ');
end
