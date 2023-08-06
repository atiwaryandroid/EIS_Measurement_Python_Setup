%% Destruct FPGA
%    FPGA_Destruct(xptr);
%% connect and program FPGA
clear all
close all
[ mlist,snlist,xem,xptr ] = FPGA_Config('C:\Users\Aaryan\EIS_V1p1\EIS_V1p1\top_eis.bit');
fprintf('==========================================\n');
fprintf('Start testing %s\n',datestr(now,'HH:MM:SS')); 
fprintf('==========================================\n');

%% setup parameter
t_measure = 1;
test_scan_in   = '0';    %'1': test scan chain of test structure, '0': normal operation
load_source    = '1';    %'1': trigger one time asynchronous, '0': the same as S_CLK
en_clk_c       = '0';    %'1': enable, '0': disable
rst_pd        = '1';    %'1': normal operation, '0': reset phase detector
trimrf0       = '0';    %'1': enable 7.5k Rf parallel resistor
trimrf1       = '0';    %'1': enable 20k Rf parallel resistor
ref_sel        = '0 ';    %'1': ext                                                                                                                                                                                                                                                                                                           , '0': from ref pixel                            //Bypass ref pixel in test structure and array for characterization//
ref_sel_ext    = '0';    %'1': w/ inv chain, '0' w/o inv chain                     //Option for ext clock used when ref pixel bypassed in array//
no_col_readout = '0000'; % '0000' to '1111' readout # of columns "no_col_readout+1" //Select how many columns to read, 1 to 16//

%TDC sampling frequency = Fclk/N, N>=21 (limited due to scan chain, it further dcreases when reading out rows
%% set ref clk frequency
f_ref_clk    = 10e6;                               % unit: Hz, max: 100MHz
t_ref_clk    = 100e6/2/f_ref_clk;                   % f_clk = 100M/2/data_hr_sw
setwireinvalue(xem, hex2dec('04'),t_ref_clk,hex2dec('ffffffff'));

%% set scan clk frequency
f_scan_clk    = 1e6;                                 % unit: Hz, max: 10MHz
t_scan_clk    = floor(100e6/2/f_scan_clk/4);         % f_clk = 100M/2/data_hr_sw  
setwireinvalue(xem, hex2dec('02'),t_scan_clk,hex2dec('ffffffff'));   % Send the ratio between sys clock and scan clock

f_scan_real = 100e6/t_scan_clk/2/4/21;
fprintf('scan rate is set as %d\n',f_scan_real); %%  //  Read the whole thing out - datalength = 21  //

%%
pulsevals = 5;
%for i=1:1
    %% test TDC
    %t_pulse_tdc    = 10;                 % unit: 10ns
    %t_pulse_tdc = pulsevals(i);
    %setwireinvalue(xem, hex2dec('03'),t_pulse_tdc,hex2dec('ffffffff'));
    %updatewireins(xem);

    %% chip mode
    %  Control Signals at wirein('00')
    %  31: SC_clk_enb
    %  30: SC_data_enb
    %  29: test scan chain, '1': test scan chain, '0': normal operation
     % test_EIS_scan_chain

    %% read out FIFO from FPGA
    %pause(t_measure);
    %FPGA_read_teststr_loop
%end   

t_pulse_tdc = pulsevals;
setwireinvalue(xem, hex2dec('03'),t_pulse_tdc,hex2dec('ffffffff'));
updatewireins(xem);

%% chip mode
%  Control Signals at wirein('00')
%  31: SC_clk_enb
%  30: SC_data_enb
%  29: test scan chain, '1': test scan chain, '0': normal operation
test_EIS_scan_chain

%% read out FIFO from FPGA
pause(t_measure);
%FPGA_read_teststr_loop
FPGA_read_array

    %% Destruct FPGA
    FPGA_Destruct(xptr);
