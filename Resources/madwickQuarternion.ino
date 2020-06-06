void MadgwickQuaternionUpdate(float ax, float ay, float az, float gx, float gy, float gz, float mx, float my, float mz)
{
float q1 = q[0], q2 = q[1], q3 = q[2], q4 = q[3]; //  local variables
float norm;
float hx, hy, _2bx, _2bz;
float s1, s2, s3, s4;
float qDot1, qDot2, qDot3, qDot4;
//  variables to avoid repeated formulas
float _2q1mx;
float _2q1my;
float _2q1mz;
float _2q2mx;
float _4bx;
float _4bz;
float _2q1 = 2.0f * q1;
float _2q2 = 2.0f * q2;
float _2q3 = 2.0f * q3;
float _2q4 = 2.0f * q4;
float _2q1q3 = 2.0f * q1 * q3;
float _2q3q4 = 2.0f * q3 * q4;
float q1q1 = q1 * q1;
float q1q2 = q1 * q2;
float q1q3 = q1 * q3;
float q1q4 = q1 * q4;
float q2q2 = q2 * q2;
float q2q3 = q2 * q3;
float q2q4 = q2 * q4;
float q3q3 = q3 * q3;
float q3q4 = q3 * q4;
float q4q4 = q4 * q4;


// Normalise accelerometer measurement
norm = sqrt(ax * ax + ay * ay + az * az);
if (norm == 0.0f) return; // handle NaN
norm = 1.0f/norm;
ax *= norm;
ay *= norm;
az *= norm;
// Normalise magnetometer measurement
norm = sqrt(mx * mx + my * my + mz * mz);
if (norm == 0.0f) return; // handle NaN
norm = 1.0f/norm;
mx *= norm;
my *= norm;
mz *= norm;
// Reference direction of Earth’s magnetic field
_2q1mx = 2.0f * q1 * mx;
_2q1my = 2.0f * q1 * my;
_2q1mz = 2.0f * q1 * mz;
_2q2mx = 2.0f * q2 * mx;
hx = mx * q1q1 – _2q1my * q4 + _2q1mz * q3 + mx * q2q2 + _2q2 * my * q3 + _2q2 * mz * q4 – mx * q3q3 – mx * q4q4;
hy = _2q1mx * q4 + my * q1q1 – _2q1mz * q2 + _2q2mx * q3 – my * q2q2 + my * q3q3 + _2q3 * mz * q4 – my * q4q4;
_2bx = sqrt(hx * hx + hy * hy);
_2bz = -_2q1mx * q3 + _2q1my * q2 + mz * q1q1 + _2q2mx * q4 – mz * q2q2 + _2q3 * my * q4 – mz * q3q3 + mz * q4q4;
_4bx = 2.0f * _2bx;
_4bz = 2.0f * _2bz;
