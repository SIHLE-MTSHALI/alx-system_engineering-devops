#!/usr/bin/env ruby
# This script searches for a pattern with repetition tokens

puts ARGV[0].scan(/hbt{2,5}n/).join
