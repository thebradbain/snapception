# This script takes an encrypted Snapchat image and decrypts it into its
# original JPEG format.

# This script is taken from AJ Jenkins, who in turn borrowed and adapted much of it from Amelia Cuss. 
# See the README for more details.

require 'openssl'

if ARGV.length == 2

    encrypted_image = ARGV[0]
    decrypted_image = ARGV[1] 

    data = File.open(encrypted_image, 'r').read
    c = OpenSSL::Cipher.new('AES-128-ECB')
    c.decrypt
    c.key = 'M02cnQ51Ji97vwT4'
    o = ''.force_encoding('ASCII-8BIT')
    data.bytes.each_slice(16) {|s| o += c.update(s.map(&:chr).join)}
    File.open(decrypted_image, 'w') {|f| f.write(o) }

else
    puts "Syntax Error: use 'ruby decrypt_snap.rb input_file output_file.jpg'"
end
