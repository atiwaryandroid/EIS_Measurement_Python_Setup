%% FPGA readout
%close all;
%figure;
fprintf('reading data from FPGA\n');
time_run = datestr(now,'_yyyy-mm-dd_HHMMSS');
data_points = 2^12;
data_read_leng = 2^10;
test_len = 2^10;
data_transient(:)=0;
no_col = 16;
%f2=figure;
Color = {'k','b','r','g','y','c','m',[0.87 0.49 0],[0 0.75 0.75],[0 0.5 0],[0.75 0.75 0],[0.75 0 0.75],[0.5 0.5 0.5 ],[1 0.6 0.78],[0.6 0.2 0],[.8 .2 .6]} ;% Cell array of colors.
    
%data_pipeout_old_1  = readfromblockpipeout(xem, hex2dec('a0'), data_read_leng, 4*data_points);
%data_pipeout_old_2  = readfromblockpipeout(xem, hex2dec('a1'), data_read_leng, 4*data_points);
%data_pipeout_old_3  = readfromblockpipeout(xem, hex2dec('a2'), data_read_leng, 4*data_points);
%data_pipeout_old_4  = readfromblockpipeout(xem, hex2dec('a3'), data_read_leng, 4*data_points);
%data_pipeout_old_5  = readfromblockpipeout(xem, hex2dec('a4'), data_read_leng, 4*data_points);
%data_pipeout_old_6  = readfromblockpipeout(xem, hex2dec('a5'), data_read_leng, 4*data_points);
%data_pipeout_old_7  = readfromblockpipeout(xem, hex2dec('a6'), data_read_leng, 4*data_points);
%data_pipeout_old_8  = readfromblockpipeout(xem, hex2dec('a7'), data_read_leng, 4*data_points);
    
%data_pipeout_old_9  = readfromblockpipeout(xem, hex2dec('a8'), data_read_leng, 4*data_points);
%data_pipeout_old_10 = readfromblockpipeout(xem, hex2dec('a9'), data_read_leng, 4*data_points);
%data_pipeout_old_11 = readfromblockpipeout(xem, hex2dec('aa'), data_read_leng, 4*data_points);
%data_pipeout_old_12 = readfromblockpipeout(xem, hex2dec('ab'), data_read_leng, 4*data_points);
%data_pipeout_old_13 = readfromblockpipeout(xem, hex2dec('ac'), data_read_leng, 4*data_points);
%data_pipeout_old_14 = readfromblockpipeout(xem, hex2dec('ad'), data_read_leng, 4*data_points);
%data_pipeout_old_15 = readfromblockpipeout(xem, hex2dec('ae'), data_read_leng, 4*data_points);
%data_pipeout_old_16 = readfromblockpipeout(xem, hex2dec('af'), data_read_leng, 4*data_points);
    
%data_pipeout_old_17 = readfromblockpipeout(xem, hex2dec('b0'), data_read_leng, 4*data_points);
%data_pipeout_old_18 = readfromblockpipeout(xem, hex2dec('b1'), data_read_leng, 4*data_points);
%data_pipeout_old_19 = readfromblockpipeout(xem, hex2dec('b2'), data_read_leng, 4*data_points);
%data_pipeout_old_20 = readfromblockpipeout(xem, hex2dec('b3'), data_read_leng, 4*data_points);
%pause(0.5);


for k=1:1:test_len
    fprintf('Run #%d\n',k);
    tic;
    data_pipeout(1,:)  = readfromblockpipeout(xem, hex2dec('a0'), data_read_leng, 4*data_points);
    data_pipeout(2,:)  = readfromblockpipeout(xem, hex2dec('a1'), data_read_leng, 4*data_points);
    data_pipeout(3,:)  = readfromblockpipeout(xem, hex2dec('a2'), data_read_leng, 4*data_points);
    data_pipeout(4,:)  = readfromblockpipeout(xem, hex2dec('a3'), data_read_leng, 4*data_points);
    data_pipeout(5,:)  = readfromblockpipeout(xem, hex2dec('a4'), data_read_leng, 4*data_points);
    data_pipeout(6,:)  = readfromblockpipeout(xem, hex2dec('a5'), data_read_leng, 4*data_points);
    data_pipeout(7,:)  = readfromblockpipeout(xem, hex2dec('a6'), data_read_leng, 4*data_points);
    data_pipeout(8,:)  = readfromblockpipeout(xem, hex2dec('a7'), data_read_leng, 4*data_points);

    data_pipeout(9,:)  = readfromblockpipeout(xem, hex2dec('a8'), data_read_leng, 4*data_points);
    data_pipeout(10,:) = readfromblockpipeout(xem, hex2dec('a9'), data_read_leng, 4*data_points);
    data_pipeout(11,:) = readfromblockpipeout(xem, hex2dec('aa'), data_read_leng, 4*data_points);
    data_pipeout(12,:) = readfromblockpipeout(xem, hex2dec('ab'), data_read_leng, 4*data_points);
    data_pipeout(13,:) = readfromblockpipeout(xem, hex2dec('ac'), data_read_leng, 4*data_points);
    data_pipeout(14,:) = readfromblockpipeout(xem, hex2dec('ad'), data_read_leng, 4*data_points);
    data_pipeout(15,:) = readfromblockpipeout(xem, hex2dec('ae'), data_read_leng, 4*data_points);
    data_pipeout(16,:) = readfromblockpipeout(xem, hex2dec('af'), data_read_leng, 4*data_points);
    
    data_pipeout(17,:) = readfromblockpipeout(xem, hex2dec('b0'), data_read_leng, 4*data_points);
    data_pipeout(18,:) = readfromblockpipeout(xem, hex2dec('b1'), data_read_leng, 4*data_points);
    data_pipeout(19,:) = readfromblockpipeout(xem, hex2dec('b2'), data_read_leng, 4*data_points);
    data_pipeout(20,:) = readfromblockpipeout(xem, hex2dec('b3'), data_read_leng, 4*data_points);
    pause(0.1);
    
%     close all;
    data_out(1:1:8,1:1:data_points) = 0;
    %data_out_2(1:1:8,1:1:data_points) = 0;
    timeinterval =toc;
    for j = 17:1:19
        data_out(j,:) = mod(double(data_pipeout(j,2:4:end)),2^6)*2^8 + double( data_pipeout(j,1:4:end));
        length_data = no_col*fix(length(data_out(j,:))/no_col);
        data_out_truncated(j,:) = data_out(j,1:length_data);
        for m = 1:1:no_col
            data_out_pixel (m ,:)= data_out_truncated(j,(m:no_col:end));
            data_transient (j,m,k,1)= cnt_diff(data_out_pixel (m ,:))/no_col;
            
            if (k==1)
                data_transient (j,m,k,2) = 0;
            end
            if (k>1)
                data_transient (j,m,k,2) = data_transient (j,m,k-1,2)+timeinterval;
            end
            subplot(4,5,j);
            scatter((data_transient(j,m,:,2))/60,(data_transient(j,m,:,1)),10,Color{m},'filled','DisplayName',int2str(m));drawnow
            hold on

        end
        hold off
        title(['Transient Plot of Row # ', int2str(j)]);
        hold on
    end
        [h, ~] =legend ('show');
        h.FontSize =5;
        
        hold on
end
    time_run = datestr(now,'_yyyy-mm-dd_HHMMSS');
    File_Name = ['TDC_array_transient' time_run '.csv'];
    sdir = 'C:\Users\Aaryan\EIS_V1p1\EIS_V1p1\dlmwritefolder';
    for x = 1:1:20
        for y = 1:1:no_col
              dlmwrite(sprintf('%s\\%s',sdir,File_Name), data_transient(x,y,:,1) ,'-append');
              dlmwrite(sprintf('%s\\%s',sdir,File_Name), data_transient(x,y,:,2),'-append');
        end 
    end