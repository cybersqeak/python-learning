This project demonstrates numerical simulation of electron motion
under uniform electric and magnetic fields using Python.

# Electron Motion in Uniform Electric and Magnetic Fields

This project simulates the motion of an electron inside an idealized infinite solenoid,
where a uniform magnetic field **B** and a uniform electric field **E** are applied.

The electron dynamics are calculated using the **Lorentz force equation** and integrated
numerically in time. The trajectory is visualized in 3D and exported as image frames
that can be combined into a video or GIF.

## Physics Model

The motion follows the Lorentz force law:

F = -e ( E + v × B )

where:
- e : elementary charge
- v : electron velocity
- E : electric field
- B : magnetic field

The equation of motion is solved using the explicit Euler method.

## Parameters

- Magnetic field: B = (0, 0, 0.05) T
- Electric field: E = (0, 100, 0) V/m
- Initial velocity: v = (1e5, 1e5, 1e5) m/s
- Time step: dt = 1e-11 s

## Output

Each simulation step is saved as a PNG image.
These images can be combined into a video using ffmpeg.

Example:
```bash
ffmpeg -framerate 30 -i %d.png -c:v libx264 output.mp4
