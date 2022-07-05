-- Advent of Code 2015 day 01 part one

io.input("../inputs/01-input.txt")

local floor = 0
local index = 1
local directions = { ['('] = 1, [')'] = -1 }

while true do
    local inst = io.read(1)
    if (inst == nil) then
        break
    elseif directions[inst] ~= nil then
        floor = floor + directions[inst]
    else
        io.stderr:write("Invalid character found at position '" .. index .. "'\n")
        os.exit(1)
    end
    index = index + 1
end

print("The right floor is '" .. floor .. "'")
