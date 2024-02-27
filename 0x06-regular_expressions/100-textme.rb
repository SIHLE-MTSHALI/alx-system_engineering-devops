#!/usr/bin/env ruby
# This script outputs sender, receiver, and flags from a log

log_line = ARGV[0]
sender = log_line.match(/\[from:(.+?)\]/)[1]
receiver = log_line.match(/\[to:(.+?)\]/)[1]
flags = log_line.match(/\[flags:(.+?)\]/)[1]

puts "#{sender},#{receiver},#{flags}"
