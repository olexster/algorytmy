localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
# host i port muszą wskazywać na adres uruchomionego serwera danych
ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
sesja = ctx.ServiceManager.createInstanceWithContext( "com.sun.star.frame.Desktop", ctx)