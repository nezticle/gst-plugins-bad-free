/*
 * GStreamer
 * Copyright (C) 2009 Nokia Corporation <multimedia@maemo.org>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */
#ifndef __GST_CAMERABIN_PERFORMANCE_H__
#define __GST_CAMERABIN_PERFORMANCE_H__

#ifdef HAVE_CONFIG_H
#   include <config.h>
#endif

/*
 * performance timestamping
 */
#ifdef GST_TIMESTAMPS
#   ifndef ENTER
#       include <stdio.h>
#       include <sys/time.h>
#       include <time.h>
#       define TIMESTAMP struct timeval timestamp_for_time_tracking; gettimeofday(&timestamp_for_time_tracking,NULL);
#       define TIMESTAMPLONG (timestamp_for_time_tracking.tv_sec*1000000ll+timestamp_for_time_tracking.tv_usec)
#       define ENTER { TIMESTAMP; fprintf(stderr,"ENTERING:%s:%lli:\n",__func__,TIMESTAMPLONG); };
#       define LEAVE { TIMESTAMP; fprintf(stderr,"LEAVING:%s:%i:%lli:\n",__func__,__LINE__,TIMESTAMPLONG);  };
#       define CP(name) { TIMESTAMP; fprintf(stderr,"CHECKPOINT:%s:%s:%i:%lli:\n",name,__func__,__LINE__,TIMESTAMPLONG);  };
#   endif
#else
#   define TIMESTAMP
#   define TIMESTAMPLONG
#   define ENTER
#   define LEAVE
#   define CP(name)
#endif


#endif /* #ifndef __CAMERABIN_PERFORMANCE_H__ */
