#!/usr/bin/env ruby
# This script uses regex to match patterns with zero or more occurrences of 't'

puts ARGV[0].scan(/hbt*n/).join
