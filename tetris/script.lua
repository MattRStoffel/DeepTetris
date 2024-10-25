-- Function to save addresses in CSV format to a text file
function save_addresses_to_csv(start_addr, end_addr, file)
	for addr = start_addr, end_addr do
		local value = memory.readbyteunsigned(addr)
		file:write(string.format("%02x", value))
	end
	-- Ensure the last line ends with a newline
	file:write(",")
end

-- Function to convert values to binary (0 if value == 0xEF, 1 otherwise)
function convert_to_binary(start_addr, end_addr, file)
	for addr = start_addr, end_addr do
		local value = memory.readbyteunsigned(addr)
		if value == 0xEF then
			file:write("0")
		else
			file:write("1")
		end
	end
	file:write(",")
end

local output_file = io.open("data/addresses_output.csv", "w")

local x = 1
local run = true
while run do
	if output_file then
		output_file:write(x .. ",")
		save_addresses_to_csv(0x00F7, 0x00F7, output_file)
		convert_to_binary(0x0400, 0x04C7, output_file)
		save_addresses_to_csv(0x0200, 0x020F, output_file)
		output_file:write("\n")
	end

	gui.savescreenshotas("data/images/screenshot" .. x .. ".png")
	x = x + 1
	FCEU.frameadvance()
	if emu.framecount() >= 10000 then
		run = false
		output_file:close()
		emu.exit()
	end
end
