%% chip mode
%  Control Signals at wirein('00')
%  31: SC_clk_enb
%  30: SC_data_enb
%  29: test scan chain
%  28: load source
%  27: en_clk_c
%  26: ref_sel
%  25-0: unused

test_len = 2^16;
total_error(1:1:test_len) = 0;
result_s_in(1:1:test_len) = floor(rand(test_len,1)'*2^21-1);
result_s_out(1:1:test_len) = 0;

%% scan data
wirein_26bit = '00 0000 0000 0000 0000 0000 0000';
s_data_reset    = bin2dec(strcat('11',test_scan_in,load_source,en_clk_c,ref_sel,wirein_26bit));
s_data_clk_only = bin2dec(strcat('01',test_scan_in,load_source,en_clk_c,ref_sel,wirein_26bit));
s_data_run      = bin2dec(strcat('00',test_scan_in,load_source,en_clk_c,ref_sel,wirein_26bit));
sc_unused = '0000 0000 000'; 
    
for j = 0:1:test_len-1
%     s_data_in    = j; 
      s_data_in    = result_s_in(j+1);
%     s_data_in    = bin2dec(strcat(sc_unused,'0 00000 11000 10100 00000'));

    %% program test chip (setup scan chain value)
    % reset
    setwireinvalue(xem, hex2dec('00'),s_data_reset,   hex2dec('ffffffff'));
    updatewireins(xem);
%     pause(1e-3);

    % turn on the scan chain (SCLK on)
    setwireinvalue(xem, hex2dec('00'),s_data_clk_only,hex2dec('ffffffff'));
    updatewireins(xem);
%     pause(1e-3);

    % start of scan in (shift in and trigger load)
    setwireinvalue(xem, hex2dec('00'),s_data_run,  hex2dec('ffffffff'));
    setwireinvalue(xem, hex2dec('01'),s_data_in,   hex2dec('ffffffff'));
    updatewireins(xem);
%     fprintf('Scan in.................\n');
%     pause(0.1);
%     fprintf('Scan out................\n');
%     pause(0.1);

    % read data in
    updatewireouts(xem);
    data_out = getwireoutvalue(xem, hex2dec('20'));   % data from counter and comparator
%     pause(1e-3);

    %% test the scan out by comparing the scan in
    if test_scan_in == '1'
        % start of scan in (disable load)
%         setwireinvalue(xem, hex2dec('00'),s_data_clk_only,hex2dec('ffffffff'));
%         updatewireins(xem);
%         pause(1e-3);

        % turn off of scan in (SCLK off)
%         setwireinvalue(xem, hex2dec('00'),s_data_reset,   hex2dec('ffffffff'));
%         updatewireins(xem);
%         pause(1e-3);

        % verify the scan data
        % be careful the reversed order of scan-in and scan-out
        s_in       = dec2binarray32(s_data_in);
        s_out      = dec2binarray32(data_out);   % data from counter and comparator 
        error = 0;
        for i=1:21
            if(s_in(22-i) ~= s_out(i))
%                 fprintf('the %d-th bit is incorrect!\n',i);
                error = 1;
           end
        end
%         if (error == 0)
%             fprintf('scan chain %d is CORRECT :)\n',j);
%         end 
        if (mod(j,100) == 0 && j~=0)
               fprintf('scan chain %d is done\n',j);
               k = find(total_error(j-100+1:j))
        end
    end
    result_s_out(j+1) = bi2de(fliplr(s_out(1:21)));
    total_error(j+1) = error;
end

k = find(total_error)