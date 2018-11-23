#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <time.h>
#include <string.h>
#include <string>

#define RPMSG_BUF_SIZE    512

int fd;
char msg_buff[RPMSG_BUF_SIZE];

extern "C"{

int open_pru(std::string fname)
{
  char file[80];
  sprintf(file, "/dev/rpmsg_pru%s", fname.c_str());
  fd = open(file, O_RDWR);
  if(fd < 0)
  {
    return -1;
  }
    memset(msg_buff, '\0', RPMSG_BUF_SIZE);
  return 0;
}

int32_t read_speed(uint32_t motor)
{
  return 1;
}


int32_t write_speed(uint32_t motor)
{
  return 1;
}

int32_t write_gains(uint32_t motor, float ki, float kd, float kp)
{
  return 1;
}
}
