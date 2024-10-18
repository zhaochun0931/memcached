import memcache

client = memcache.Client(['my-memcache:11211'], debug=1)
client.set('my_key', 'value')
value = client.get('my_key')
print(value)  # Should print 'value'
