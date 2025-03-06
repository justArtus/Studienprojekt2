export async function fetchProducts() {
    const response = await fetch('http://localhost:8000/api/products/');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
}