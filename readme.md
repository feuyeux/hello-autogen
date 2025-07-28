# Hello Autogen

- https://github.com/microsoft/autogen/tags
- https://github.com/ag2ai/ag2/tags

<https://microsoft.github.io/autogen/stable>

> The whole is greater than the sum of its parts.
>
> -- Aristotle

## run

```sh
source autogen_env/Scripts/activate
```

### 1 run with ollama llama3

- <https://www.litellm.ai/>
- <https://github.com/BerriAI/litellm>
- <https://microsoft.github.io/autogen/docs/topics/non-openai-models/local-litellm-ollama>

```sh
ollama pull llama3
ollama list
```

```sh
python hello_autogen_llama3.py
```

### 2 run with huggingface gemma

```sh
# https://huggingface.co/settings/tokens
export HUGGINGFACE_API_KEY=''
litellm --model huggingface/google/gemma-2b-it
```

```sh
python hello_autogen_gemma.py
```

### 3 run with moonshot

```sh
# https://platform.moonshot.cn/console/api-keys
echo "MOONSHOT_API_KEY=" > .env

python hello_autogen_moonshot.py
```
