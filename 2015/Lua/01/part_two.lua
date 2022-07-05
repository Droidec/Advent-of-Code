-- Advent of Code 2015 day 01 part two

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

    if floor == -1 then
        print("Basement is reached at position '" .. index .. "'")
        os.exit(0)
    end
    index = index + 1
end

io.stderr:write("The basement was never reached?\n")
os.exit(1)
