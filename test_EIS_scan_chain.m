%% chip mode
%  Control Signals at wirein('00')
%  31: SC_clk_enb
%  30: SC_data_enb
%  29: test scan chain
%  28: load source
%  27: en_clk_c
%  26: ref_sel
%  25: ref_sel_ext
%  24-4: unused
%  3-0: Col_readout

%% scan data
wirein_18bit = '00 0000 0000 0000 0000';
s_data_reset    = bin2dec(strcat('11',test_scan_in,load_source,en_clk_c,ref_sel,ref_sel_ext,rst_pd, trimrf0, trimrf1, wirein_18bit,no_col_readout));
s_data_clk_only = bin2dec(strcat('01',test_scan_in,load_source,en_clk_c,ref_sel,ref_sel_ext,rst_pd, trimrf0, trimrf1, wirein_18bit,no_col_readout));
s_data_run      = bin2dec(strcat('00',test_scan_in,load_source,en_clk_c,ref_sel,ref_sel_ext,rst_pd, trimrf0, trimrf1, wirein_18bit,no_col_readout));

sc_unused = '0000 0000 000';
%  s_data_in    = bin2dec(strcat(sc_unused,'1 00110 10011 10100 10001'));
% s_data_in    = bin2dec(strcat(sc_unused,'0 00000 11000 10100 00000'));
s_data_in    = (2^27)-1;

%% program test chip (setup scan chain value)
% reset
setwireinvalue(xem, hex2dec('00'),s_data_reset,   hex2dec('ffffffff'));     %% '00' is used to control various control bits %%
updatewireins(xem);
pause(0.2);

% turn on the scan chain (SCLK on)
setwireinvalue(xem, hex2dec('00'),s_data_clk_only,hex2dec('ffffffff'));
updatewireins(xem);
pause(0.05);

% start of scan in (shift in and trigger load)
setwireinvalue(xem, hex2dec('00'),s_data_run,  hex2dec('ffffffff'));
if test_scan_in == '1'
setwireinvalue(xem, hex2dec('01'),bin2dec('0000 1111 0000 0000  0100 1111 0100 1111'),hex2dec('ffffffff'));
updatewireins(xem);
end
if test_scan_in == '0'
setwireinvalue(xem, hex2dec('01'),bin2dec('1111 1111 1111 1111  1111 1111 1111 1111'),hex2dec('ffffffff'));
updatewireins(xem);
end
fprintf('Scan in.................\n');
pause(0.1);
fprintf('Scan out................\n');
pause(0.1);

% read data in
updatewireouts(xem);
data_out = getwireoutvalue(xem, hex2dec('20'));   % data from counter and comparator
pause(0.1);

%% test the scan out by comparing the scan in
if test_scan_in == '1'
    % start of scan in (disable load)
    setwireinvalue(xem, hex2dec('00'),s_data_clk_only,hex2dec('ffffffff'));
    updatewireins(xem);
    pause(0.1);

    % turn off of scan in (SCLK off)
    setwireinvalue(xem, hex2dec('00'),s_data_reset,   hex2dec('ffffffff'));
    updatewireins(xem);
    pause(0.1);

    % verify the scan data
    % be careful the reversed order of scan-in and scan-out
    s_in       = dec2binarray32(bin2dec('0000 0000 000 0 0000  0100 1111 0100 1111'));
    s_out      = dec2binarray32(data_out);   % data from counter and comparator 
    error = 0;
    for i=1:21
        if(s_in(22-i) ~= s_out(i))
            fprintf('the %d-th bit is incorrect!\n',i);
            error = 1;
       end
    end
    if (error == 0)
        fprintf('scan chain is CORRECT :)\n');
    end 
end