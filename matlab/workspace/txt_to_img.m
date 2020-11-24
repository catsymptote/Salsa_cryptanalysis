clc
clear


for folder_index=1:200
    if(folder_index <10)
    dir_name = char(strcat('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\_images_from_kiran\train\00', num2str(folder_index), '\'));
    elseif(folder_index<100)
        dir_name = char(strcat('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\_images_from_kiran\train\0', num2str(folder_index), '\'));
    else
    dir_name = char(strcat('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\_images_from_kiran\train\', num2str(folder_index), '\'));
    end
    
    images = dir(char(strcat(dir_name, '\*lg.code')));



    for image_index = 1:5
        % Get file names and paths.
        file_name = images(image_index).name;
        read_path = fullfile(dir_name, file_name);
        write_path= fullfile(dir_name, file_name); write_path = char(strrep(write_path, '_lg.code', '_lg_PT.png'));
        disp(file_name);
        disp(read_path);
        disp(write_path);


        % Read files.
        %image_data = imread('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\test_image2.jpg');
        file_data = fileread(read_path);

        for idx = 1:length(file_data)
            converted_text(idx) = unicode2native(file_data(idx));

        end

        converted_text = converted_text(1:2610);

        %reshape image_data = imreshape(image_data, [256 256]); imwrite
        converted_image = reshape(converted_text, [261 10]);%[306*2 268]);
        converted_image = imresize(converted_image', [256 256]);%[306*2 268]);256
        %converted_image = cat(3, converted_image, converted_image, converted_image);

        %imshow(mat2gray(converted_image - mean(mean(converted_image))), [])

        imwrite(uint8((converted_image)), write_path)

%         
%         % Read files.
%         %image_data = imread('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\test_image2.jpg');
%         image_data = imread(read_path);
%         image_data = imresize(image_data, [256 256]);
%         image_data = image_data(:,:,1);
%         image_data = image_data(:);
%     
%         for idx = 1:length(image_data)
%             converted_text(idx) = unicode2native(char(image_data(idx)));
%         end
%     
%         %reshape image_data = imreshape(image_data, [256 256]); imwrite
%         %converted_text = reshape(converted_text, [256 256]);
%     
%         % Write files.
%         %fileID = fopen('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\test_image2.txt','w');
%         %fileID = fopen(write_path,'w');
%         %fwrite(fileID, converted_text, 'uint8');
%         %fclose(fileID);
%         
%         %dlmwrite('D:\Projects\MasterThesis\Salsa_cryptanalysis\matlab\images\PT_txt\test.txt',converted_text,'delimiter',' ');
%         dlmwrite(write_path,converted_text,'delimiter',' ');
    end
end
