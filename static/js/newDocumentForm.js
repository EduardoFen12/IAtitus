async function sendInput(title, author, content) {
	const response = await fetch("http://127.0.0.1:5000/newDocumentForm", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			title: title,
			author: author,
			content: content,
		}),
	});
}

document
	.getElementById("contentForm")
	.addEventListener("submit", async function (event) {
		event.preventDefault();

		const title = document.getElementById("title").value;
		const author = document.getElementById("author").value;
		const content = document.getElementById("content").value;

		try {
			await sendInput(title, author, content);
			document.getElementById("successMessage").style.display = "block";

			document.getElementById("contentForm").reset();
		} catch (error) {
			console.error("Erro ao enviar dados:", error);
		}
	});
