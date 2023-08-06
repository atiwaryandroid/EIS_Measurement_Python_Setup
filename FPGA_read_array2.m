%% FPGA readout for Hourglass ADC
%close all;
%figure;
fprintf('==========Reading data from FPGA==========\n');
time_run = datestr(now,'_yyyy-mm-dd_HHMMSS');
data_points = 2^11;
data_read_leng = 2^10;

no_freq  = 6;
freq     = [5 10 25 50 75 100]*1e3;
% no_freq  = 1;
% freq     = 50e3;
phase    = 270;
% phase    = (0:5:360);
Vos      = 1.2;
Vsin_pp  = 50e-3;

for k=1:1:150
    for f = 1:1:no_freq 
        fprintf('Run #%d-%d\n',k,f);
        %fg = FunctionGeneratorControllerSinSqr(freq(f), phase, Vsin_pp, Vos);
%         fg = FunctionGeneratorControllerSinSqr(freq(f), phase(k), Vsin_pp, Vos);

        %pause(1);
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

        pause(0.5);
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


        close all;
        data_out(1:1:8,1:1:data_points) = 0;
        for j = 1:1:20
            data_out(j,:) = mod(double(data_pipeout(j,2:4:end)),2^6)*2^8 + double( data_pipeout(j,1:4:end));
            if mod(j,5)  == 0
    %         if j == 20
                figure;
                plot(data_out(j,:),'o-');
            end   
        end
%         fprintf('        Row5_cnt_avg = %f\n',cnt_diff(data_out(5,:)));
%         fprintf('        Row10_cnt_avg = %f\n',cnt_diff(data_out(10,:)));
%         fprintf('        Row15_cnt_avg = %f\n',cnt_diff(data_out(15,:)));
%         fprintf('        Ref_cnt_avg = %f\n',cnt_diff(data_out(20,:)));

        %% write data
        File_Name = ['ASSAY' sprintf('-%d-Freq%d',k,f) time_run '.csv'];
        sdir = 'C:\Users\Aaryan\EIS_V1p1\EIS_V1p1\EIS_Edwin\FPGA_EIS_V1_array_18rows_EDWIN';
        csvwrite(sprintf('%s\\%s',sdir,File_Name), data_out');

    %     pause(1);
    %     pause(0.25*60);
%         pause(10);
    end
end
