-- run.lua

local button_map = {
	--	[10] = "start",
	[40] = "A",
	[80] = "B",
	[02] = "left",
	[01] = "right",
	[04] = "down",
	[08] = "up",
}

local function get_closest_button(value)
	local closest_value = nil
	local closest_button = "unknown"
	local min_diff = math.huge

	for k, v in pairs(button_map) do
		local diff = math.abs(k - value)
		if diff < min_diff then
			min_diff = diff
			closest_value = k
			closest_button = v
		end
	end

	return closest_button
end

function save_addresses_to_csv(start_addr, end_addr, file)
	for addr = start_addr, end_addr do
		local value = memory.readbyteunsigned(addr)
		file:write(string.format("%02x", value))
	end
end

function SaveData(file)
	--	save_addresses_to_csv(0x00F7, 0x00F7, file)
	save_addresses_to_csv(0x0400, 0x04C7, file)
	save_addresses_to_csv(0x0200, 0x020F, file)
end

local x = 1
local run = true

while run do
	local output_file = io.open("active.csv", "w")

	if output_file then
		--		output_file:write("frame,input,board\n")
		SaveData(output_file)
		output_file:close()
	end

	local input_file = io.open("active_input.csv", "r")

	if input_file then
		local input = input_file:read("*a")
		input_file:close()
		-- if input is not nil
		input = tonumber(input)
		print(input)
		if input then
			local closest_button = get_closest_button(input)
			local joypad_input = {
				up = false,
				down = false,
				left = false,
				right = false,
				A = false,
				B = false,
				start = false,
				select = false,
			}
			joypad_input[closest_button] = true
			joypad.set(1, joypad_input)
			joypad.write(1, joypad_input)
		end
	end

	x = x + 1

	FCEU.frameadvance()
	if emu.framecount() >= 10000 then
		run = false
		emu.exit()
	end
end
