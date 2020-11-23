clear
clc

images = dir('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\CT_txt\*.txt');

for i=1:length(images)
    % Get file names and paths.
    file_name = images(i).name;
    read_path = fullfile('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\CT_txt\', file_name);
    write_path= fullfile('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\CT_img\', [file_name(1:end-4) '.jpg']);
    disp(file_name);
    disp(read_path);
    disp(write_path);
    
    % Read files.
    %image_data = imread('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\test_image2.jpg');
    file_data = fileread(read_path);

    for idx = 1:length(file_data)
        converted_text(idx) = unicode2native(file_data(idx));
        
    end
    
    converted_text = converted_text(1:164016);
    
    %reshape image_data = imreshape(image_data, [256 256]); imwrite
    converted_image = reshape(converted_text, [306*2 268]);
    %converted_image = cat(3, converted_image, converted_image, converted_image);
    
    imshow(mat2gray(converted_image - mean(mean(converted_image))), [])
    
    imwrite(uint8(converted_image), write_path)

end
