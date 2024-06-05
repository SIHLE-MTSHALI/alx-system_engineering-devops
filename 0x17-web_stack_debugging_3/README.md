# 0x17. Web stack debugging #3

## Description

This project focuses on debugging a Wordpress website running on a LAMP stack (Linux, Apache, MySQL, PHP). The goal is to identify and fix a 500 Internal Server Error using `strace` and automate the fix using Puppet.

## Files

- **0-strace_is_your_friend.pp**: Puppet manifest to fix the 500 Internal Server Error in Apache.

## Requirements

- All files are interpreted on Ubuntu 14.04 LTS.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
- Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

## Installation

To run the provided code, you need to have Puppet and puppet-lint installed. Follow these steps:

```sh
# Install ruby
apt-get install -y ruby

# Install puppet-lint
gem install puppet-lint -v 2.1.1

