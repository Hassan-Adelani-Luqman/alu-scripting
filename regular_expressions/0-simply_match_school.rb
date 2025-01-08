#!/usr/bin/env ruby

# Accepts one argument from the command line
input = ARGV[0]

# Regular expression to match 'School'
regex = /School/

# Use the match method to find the pattern in the input
if input =~ regex
  puts "Match found: #{input[regex]}"
else
  puts "No match found"
end

