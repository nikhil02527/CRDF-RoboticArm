fifo_count = ((uint16_t)data[0] << 8) | data[1];
packet_count = fifo_count/12;
for (ii = 0; ii < packet_count; ii++) {
int16_t accel_temp[3] = {0, 0, 0}, gyro_temp[3] = {0, 0, 0};
readBytes(MPU9250_ADDRESS, FIFO_R_W, 12, &data[0]); // read data for averaging
accel_temp[0] = (int16_t) (((int16_t)data[0] << 8) | data[1]  ) ;  // Form signed 16-bit integer for each sample in FIFO
accel_temp[1] = (int16_t) (((int16_t)data[2] << 8) | data[3]  ) ;
accel_temp[2] = (int16_t) (((int16_t)data[4] << 8) | data[5]  ) ;
gyro_temp[0]  = (int16_t) (((int16_t)data[6] << 8) | data[7]  ) ;
gyro_temp[1]  = (int16_t) (((int16_t)data[8] << 8) | data[9]  ) ;
gyro_temp[2]  = (int16_t) (((int16_t)data[10] << 8) | data[11]) ;
accel_bias[0] += (int32_t) accel_temp[0]; // Sum individual signed 16-bit biases to get accumulated signed 32-bit biases
accel_bias[1] += (int32_t) accel_temp[1];
accel_bias[2] += (int32_t) accel_temp[2];
gyro_bias[0]  += (int32_t) gyro_temp[0];
gyro_bias[1]  += (int32_t) gyro_temp[1];
gyro_bias[2]  += (int32_t) gyro_temp[2];
}
