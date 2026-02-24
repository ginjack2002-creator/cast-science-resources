using UnityEngine;

/// <summary>
/// Simple camera controller for zooming and panning the wildfire simulation grid.
/// </summary>
public class CameraController : MonoBehaviour
{
    public float zoomSpeed = 2f;
    public float panSpeed = 0.5f;
    public float minZoom = 3f;
    public float maxZoom = 15f;

    private Vector3 lastMousePosition;
    private bool isPanning;

    void Update()
    {
        // Zoom with scroll wheel
        float scroll = Input.GetAxis("Mouse ScrollWheel");
        if (scroll != 0f)
        {
            Camera.main.orthographicSize -= scroll * zoomSpeed;
            Camera.main.orthographicSize = Mathf.Clamp(Camera.main.orthographicSize, minZoom, maxZoom);
        }

        // Pan with middle mouse or right mouse
        if (Input.GetMouseButtonDown(1) || Input.GetMouseButtonDown(2))
        {
            isPanning = true;
            lastMousePosition = Input.mousePosition;
        }

        if (Input.GetMouseButtonUp(1) || Input.GetMouseButtonUp(2))
        {
            isPanning = false;
        }

        if (isPanning)
        {
            Vector3 delta = Input.mousePosition - lastMousePosition;
            transform.position -= new Vector3(delta.x, delta.y, 0f) * panSpeed * Time.deltaTime;
            lastMousePosition = Input.mousePosition;
        }
    }
}
