# latex2mj

Python script to convert LaTeX-styled Markdown to MathJax-styled Markdown.

Example:

```
python latex2mj.py FileIn.md FileOut.md
```

will convert a file `FileIn.md` which contains inline equations in the format `$equation$`:

```
# A file with some markdown

Which has some inline equations $\Sigma = \pi \times 3$, and also some displayed equations:

$$
\mathcal{N}(x,\mu,\Sigma) = \frac{\text{exp}(-\frac{1}{2} (x-\mu)^T \Sigma^{-1} (x-\mu))}{\sqrt{(2 \pi)^2 | \Sigma |}}
$$

But Kramdown doesn't like the single dolla sign convention for inline equations.  $\mathcal{SAD}$.
```

to the file `FileOut.md` which will contain inline equations in the format `\\( equation \\)`:

```
# A file with some markdown

Which has some inline equations \\( \Sigma = \pi \times 3 \\), and also some displayed equations:

$$
\mathcal{N}(x,\mu,\Sigma) = \frac{\text{exp}(-\frac{1}{2} (x-\mu)^T \Sigma^{-1} (x-\mu))}{\sqrt{(2 \pi)^2 | \Sigma |}}
$$

But Kramdown doesn't like the single dolla sign convention for inline equations.  \\( \mathcal{SAD} \\).
```

Copyright (c) 2018 Brendan Hasz
Licensed under the MIT License
