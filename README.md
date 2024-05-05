# 3d-render-in-turtle

![Here should be gif :/](output.gif)

Simple cpu rendering of 3D objects using turtle library. Objects consist of a transform and a mesh. You can dynamically change the mesh and the object will keep the same transform.
You can add some logic to `update` function.

Control:

| Key | Action |
|-----|--------|
| q   | Increase rotation speed around the X-axis |
| a   | Decrease rotation speed around the X-axis |
| w   | Increase rotation speed around the Y-axis |
| s   | Decrease rotation speed around the Y-axis |
| e   | Increase rotation speed around the Z-axis |
| d   | Decrease rotation speed around the Z-axis |
| k   | Move cube closer to the screen |
| l   | Move cube away from the screen |
| c   | Toggle between CubeMesh and SphereMesh |