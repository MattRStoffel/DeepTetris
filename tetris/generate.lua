-- generate.lua
function save_addresses_to_csv(start_addr, end_addr, file)
	for addr = start_addr, end_addr do
		local value = memory.readbyteunsigned(addr)
		file:write(string.format("%02x", value))
	end
end

function SaveData(file)
	save_addresses_to_csv(0x00F7, 0x00F7, file)
	file:write(",")
	save_addresses_to_csv(0x0400, 0x04C7, file)
	save_addresses_to_csv(0x0200, 0x020F, file)
	file:write("\n")
end

local output_file = io.open("data/addresses_output.csv", "w")

if output_file then
	output_file:write("frame,input,board\n")
end

local x = 1
local run = true
while run do
	if output_file then
		output_file:write(x .. ",")
		SaveData(output_file)
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
