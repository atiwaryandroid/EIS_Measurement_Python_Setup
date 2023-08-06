%% FPGA readout
%close all;
%figure;
fprintf('reading data from FPGA\n');
time_run = datestr(now,'_yyyy-mm-dd_HHMMSS');
data_points = 2^12;
data_read_leng = 2^10;
test_len = 2^4;
data_transient(:)=0;
%data_transient
%class(data_transient)
f = figure;

for k=1:1:test_len
    fprintf('Run #%d\n',k);
    tic;
%     data_pipeout_old_1  = readfromblockpipeout(xem, hex2dec('a0'), data_read_leng, 4*data_points);
%     data_pipeout_old_2  = readfromblockpipeout(xem, hex2dec('a1'), data_read_leng, 4*data_points);
%     data_pipeout_old_3  = readfromblockpipeout(xem, hex2dec('a2'), data_read_leng, 4*data_points);
%     data_pipeout_old_4  = readfromblockpipeout(xem, hex2dec('a3'), data_read_leng, 4*data_points);
%     data_pipeout_old_5  = readfromblockpipeout(xem, hex2dec('a4'), data_read_leng, 4*data_points);
%     data_pipeout_old_6  = readfromblockpipeout(xem, hex2dec('a5'), data_read_leng, 4*data_points);
%     data_pipeout_old_7  = readfromblockpipeout(xem, hex2dec('a6'), data_read_leng, 4*data_points);
%     data_pipeout_old_8  = readfromblockpipeout(xem, hex2dec('a7'), data_read_leng, 4*data_points);
%     
%     data_pipeout_old_9  = readfromblockpipeout(xem, hex2dec('a8'), data_read_leng, 4*data_points);
%     data_pipeout_old_10 = readfromblockpipeout(xem, hex2dec('a9'), data_read_leng, 4*data_points);
%     data_pipeout_old_11 = readfromblockpipeout(xem, hex2dec('aa'), data_read_leng, 4*data_points);
%     data_pipeout_old_12 = readfromblockpipeout(xem, hex2dec('ab'), data_read_leng, 4*data_points);
%     data_pipeout_old_13 = readfromblockpipeout(xem, hex2dec('ac'), data_read_leng, 4*data_points);
%     data_pipeout_old_14 = readfromblockpipeout(xem, hex2dec('ad'), data_read_leng, 4*data_points);
%     data_pipeout_old_15 = readfromblockpipeout(xem, hex2dec('ae'), data_read_leng, 4*data_points);
%     data_pipeout_old_16 = readfromblockpipeout(xem, hex2dec('af'), data_read_leng, 4*data_points);
%     
%     data_pipeout_old_17 = readfromblockpipeout(xem, hex2dec('b0'), data_read_leng, 4*data_points);
%     data_pipeout_old_18 = readfromblockpipeout(xem, hex2dec('b1'), data_read_leng, 4*data_points);
%     data_pipeout_old_19 = readfromblockpipeout(xem, hex2dec('b2'), data_read_leng, 4*data_points);
    %data_pipeout_old_20 = readfromblockpipeout(xem, hex2dec('b3'), data_read_leng, 4*data_points);


    pause(0.5);
%     data_pipeout(1,:)  = readfromblockpipeout(xem, hex2dec('a0'), data_read_leng, 4*data_points);
%     data_pipeout(2,:)  = readfromblockpipeout(xem, hex2dec('a1'), data_read_leng, 4*data_points);
%     data_pipeout(3,:)  = readfromblockpipeout(xem, hex2dec('a2'), data_read_leng, 4*data_points);
%     data_pipeout(4,:)  = readfromblockpipeout(xem, hex2dec('a3'), data_read_leng, 4*data_points);
%     data_pipeout(5,:)  = readfromblockpipeout(xem, hex2dec('a4'), data_read_leng, 4*data_points);
%     data_pipeout(6,:)  = readfromblockpipeout(xem, hex2dec('a5'), data_read_leng, 4*data_points);
%     data_pipeout(7,:)  = readfromblockpipeout(xem, hex2dec('a6'), data_read_leng, 4*data_points);
%     data_pipeout(8,:)  = readfromblockpipeout(xem, hex2dec('a7'), data_read_leng, 4*data_points);
% 
%     data_pipeout(9,:)  = readfromblockpipeout(xem, hex2dec('a8'), data_read_leng, 4*data_points);
%     data_pipeout(10,:) = readfromblockpipeout(xem, hex2dec('a9'), data_read_leng, 4*data_points);
%     data_pipeout(11,:) = readfromblockpipeout(xem, hex2dec('aa'), data_read_leng, 4*data_points);
%     data_pipeout(12,:) = readfromblockpipeout(xem, hex2dec('ab'), data_read_leng, 4*data_points);
%     data_pipeout(13,:) = readfromblockpipeout(xem, hex2dec('ac'), data_read_leng, 4*data_points);
%     data_pipeout(14,:) = readfromblockpipeout(xem, hex2dec('ad'), data_read_leng, 4*data_points);
%     data_pipeout(15,:) = readfromblockpipeout(xem, hex2dec('ae'), data_read_leng, 4*data_points);
%     data_pipeout(16,:) = readfromblockpipeout(xem, hex2dec('af'), data_read_leng, 4*data_points);
%     
%     data_pipeout(17,:) = readfromblockpipeout(xem, hex2dec('b0'), data_read_leng, 4*data_points);
%     data_pipeout(18,:) = readfromblockpipeout(xem, hex2dec('b1'), data_read_leng, 4*data_points);
%     data_pipeout(19,:) = readfromblockpipeout(xem, hex2dec('b2'), data_read_leng, 4*data_points);
    data_pipeout(20,:) = readfromblockpipeout(xem, hex2dec('b3'), data_read_leng, 4*data_points);
    %data_pipeout

    
%     close all;
    data_out(1:1:8,1:1:data_points) = 0;
    %data_out_2(1:1:8,1:1:data_points) = 0;
    timeinterval =toc;
    for j = 20:1:20
    %     j = 5;
%         for i = 1:1:data_points
%             data1 = dec2binarray(data_pipeout(j,(i-1)*4+1));
%             data2 = dec2binarray(data_pipeout(j,(i-1)*4+2));
%             data_out(j,i) = bi2de([data2(1:6) data1(1:8)]);
%             data_out(j,i) = bi2de([data1(1:8) data2(1:6)]);           
%         end
        %if (k == 5)
            %fprintf('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n')
            %mod(double(data_pipeout(j,3:4:end)),2^5)*2^2
            %fprintf('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n')
            %fix(double(data_pipeout(j,2:4:end))/2^6)
            %fprintf('CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC\n')
            %mod(double(data_pipeout(j,2:4:end)),2^6)*2^8
            %fprintf('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD\n')
            %double( data_pipeout(j,1:4:end))
            %fprintf('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\n')
        %end
        data_out(j,:) = (mod(double(data_pipeout(j,3:4:end)),2^5)*2^2+fix(double(data_pipeout(j,2:4:end))/2^6))/128  + mod(double(data_pipeout(j,2:4:end)),2^6)*2^8 + double( data_pipeout(j,1:4:end));
%         if mod(j,4)  == 0
%         if j == 20
%             plot(data_out(j,:),'o-');
%             hold on
%         end
%         end   
    
%     fprintf('        Row1_cnt_avg = %f\n',cnt_diff(data_out(1,:)));
     %if (k == 1)
     %fprintf('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n')
     %data_pipeout(20,:)
     %fprintf('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n')
     %end
     fprintf('        Ref_cnt_avg = %f\n',cnt_diff(data_out(j,:)));
    data_transient (j,k,1) = cnt_diff(data_out(j,:));
    %data_transient
    if (k==1)
        data_transient (j,k,2) = 0;
    end
    if (k>1)
    data_transient (j,k,2) = data_transient (j,k-1,2)+timeinterval;
    end
    plot(data_transient(j,:,2)/60,data_transient(j,:,1));drawnow
  %  hold on
%     File_Name = ['TDC_long_transient.csv'];
%     sdir = 'C:\Users\Adjain\Documents\MATLAB\EIS_v1p1\EIS_V1p1';
%     dlmwrite(sprintf('%s\\%s',sdir,File_Name), [cnt_diff(data_out(20,:))],'-append');
%     data_transient (j,k,1) = cnt_diff(data_out(j,:));
%     if (k==1)
%         data_transient (j,k,2) = 0;
%     end
%     if (k>1)
%     data_transient (j,k,2) = data_transient (j,k-1,2)+toc;
%     end
%     figure(f);
%     plot(data_transient(j,:,2)/60,data_transient(j,:,1));
%     hold on
%     data_transient (k,2) =datestr(now,'HHMM');
    end
end
% for j=1:1:4
%     plot(data_transient(j,:,2)/60,data_transient(j,:,1));
%     hold on
% end
hold off
% legend('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20');
 