from dhooks import Webhook, Embed

hook = Webhook('https://discordapp.com/api/webhooks/token/token')
image = ('https://picsum.photos/400/400')

embed = Embed(description=name, timestamp='now', color=0x11b668)
embed.set_author(name="Discord Test", icon_url=image)
embed.add_field(name='Inline', value='True')
embed.add_field(name='Inline', value='True')
embed.add_field(name='Inline', value='False', inline=False)
embed.set_footer(text='Test', icon_url=image)
embed.set_thumbnail(image)

hook.send(embed=embed)
