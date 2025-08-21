# Pre-loop
# loop condition
# break the loop

# Start
# Set count to 0
count = 0
# While count < 10 do
while count < 10:
#   Display count
    print(count)
#   Compute count as count + 1
    count = count + 1
# end while
# end

# Nested loops
a = 0
for i in range(5):
    for j in range(5):
        print(f"{i}: {j}: {a}")
        if a == 16:
            continue
        a = a + 1
print(a)

