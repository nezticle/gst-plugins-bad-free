plugin_LTLIBRARIES = libgstpvr.la

libgstpvr_la_SOURCES = \
	gstpvr.c \
	gstpvrbufferpool.c \
	gstpvrvideosink.c

libgstpvr_la_CFLAGS = $(GST_PLUGINS_BASE_CFLAGS) $(GST_CFLAGS) $(PVR_CFLAGS)

libgstpvr_la_LIBADD = $(GST_LIBS) $(GST_BASE_LIBS) \
	$(GST_PLUGINS_BASE_LIBS) $(X11_LIBS) -lgstvideo-$(GST_MAJORMINOR) \
	-lgstinterfaces-$(GST_MAJORMINOR) -lpvr2d -lpvrPVR2D_DRIWSEGL\
	$(PVR_LIBS) \
	$(LIBM)

libgstpvr_la_LDFLAGS = $(GST_PLUGIN_LDFLAGS)
libgstpvr_la_LIBTOOLFLAGS = --tag=disable-static

noinst_HEADERS = \
	gstpvr.h \
	gstpvrbufferpool.h \
	gstpvrvideosink.h
