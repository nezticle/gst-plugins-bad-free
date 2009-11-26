AC_DEFUN([AG_GST_TIMESTAMPS], [
AC_ARG_ENABLE(timestamps,
AC_HELP_STRING([--enable-timestamps],[enable printing timestamp information to stderr]),
[case "${enableval}" in
  yes) USE_TIMESTAMPS=yes ;;
  no)  USE_TIMESTAMPS=no ;;
  *) AC_MSG_ERROR(bad value ${enableval} for --enable-timestamps) ;;
esac],
[USE_TIMESTAMPS=no]) dnl Default value
if test x$USE_TIMESTAMPS = xyes; then
  AC_DEFINE(GST_TIMESTAMPS, 1, [Define if TIMESTAMPS statements should be compiled in])
fi
])
