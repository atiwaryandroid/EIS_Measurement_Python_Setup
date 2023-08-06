function [ mlist,snlist,xem,xptr ] = FPGA_Config(bit_filename)
%   Connect and config FPGA 
%   Returns board name, serial number, xem object and pointer to this
%   objector

%   Load library
if ~libisloaded('okFrontPanel')
	loadlibrary('okFrontPanel', 'okFrontPanelDLL.h');
end

% Try to construct an okUsbFrontPanel and open it
obj.ptr = calllib('okFrontPanel', 'okFrontPanel_Construct');
num = calllib('okFrontPanel', 'okFrontPanel_GetDeviceCount', obj.ptr);
for j=1:num
   m = calllib('okFrontPanel', 'okFrontPanel_GetDeviceListModel', obj.ptr, j-1);
   sn = calllib('okFrontPanel', 'okFrontPanel_GetDeviceListSerial', obj.ptr, j-1, '           ');
   if ~exist('snlist', 'var')
      mlist = m;
      snlist = sn;
   else
      mlist = [mlist;m];
      snlist = char(snlist, sn);
   end
end
% return
xptr = obj.ptr;


% only proceed if one device is connected
if isempty(m)
    error('error: there are no devices connected')
elseif size(m,1) > 1
    error('error: there is more than one device connected')
end

% create new pointer for XEM object and connect by serial number
xem = okusbfrontpanel(obj.ptr);
xem = openbyserial(xem,sn);
pause(0.01);
%xem
%obj.ptr
%{
% double-check to make sure FrontPanel is enabled
if isfrontpanelenabled(xem)
    fprintf('\nOpal Kelly board %s with serial number %s connected successfully\n',m,sn);
else
    error('Something went wrong programming the FPGA');
end
%}

% program bit file and check for errors
result = configurefpga(xem, bit_filename);
%result = configurefpga(xem,'C:\Users\Magneto\Documents\PC-FPGA\FPGA_TIA_DFB_V3\FPGA_PC\top_adda.bit');
if ~isequal(result,'ok_NoError')
    error('FPGA programming unsuccesfull with error code: %s',result)
else
    fprintf('FPGA programming succesfull with %s\n',bit_filename);
end

end

