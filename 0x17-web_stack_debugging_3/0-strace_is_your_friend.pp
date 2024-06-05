
### Step 3: Writing the Puppet Manifest

#### Puppet Manifest: `0-strace_is_your_friend.pp`

```pp
# Puppet manifest to fix the 500 Internal Server Error in Apache caused by incorrect permissions on a directory

exec { 'fix-wordpress':
  command => 'chown -R www-data:www-data /var/www/html',
}
