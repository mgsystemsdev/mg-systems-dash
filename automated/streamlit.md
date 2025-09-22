

# 📘 Streamlit Full Cheat Sheet

*(Nearly all commands / functions as per official API reference)*

---

## Setup & CLI

| Command / Concept | Syntax                    | Explanation                                  | Notes / Gotchas                                                   |
| ----------------- | ------------------------- | -------------------------------------------- | ----------------------------------------------------------------- |
| Install package   | `pip install streamlit`   | Installs Streamlit.                          | Keep version updated.                                             |
| Run app           | `streamlit run script.py` | Runs app locally.                            | Use correct file path.                                            |
| CLI: version      | `streamlit version`       | Shows streamlit version.                     | Useful for debugging.                                             |
| CLI: config show  | `streamlit config show`   | Show current configuration.                  | Many config options.                                              |
| CLI: cache clear  | `streamlit cache clear`   | Clear cached files/data.                     | Clears both data cache & resource cache. ([docs.streamlit.io][1]) |
| CLI: help         | `streamlit help`          | Show usage info.                             | Good to remember. ([docs.streamlit.io][1])                        |
| CLI: docs         | `streamlit docs`          | Open documentation. ([docs.streamlit.io][1]) |                                                                   |

---

## Display / “Write & Magic”

| Function                                     | Syntax                                                                                | Purpose / What It Does                                                         | Notes / Gotchas                                                      |
| -------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| `st.write(*args, **kwargs)`                  | `st.write(obj, ...)`                                                                  | The catch-all for displaying many types (text, dataframes, charts, errors...). | It infers type; can sometimes be ambiguous. ([docs.streamlit.io][2]) |
| `st.write_stream(generator, **kwargs)`       | `st.write_stream(my_generator)`                                                       | Streams content gradually (typewriter effect etc.).                            | Useful for streaming data / LLMs. ([docs.streamlit.io][3])           |
| Magic (literal values or variables on lines) | e.g. placing a variable on its own line in the script gets implicitly `st.write(...)` | Fast prototyping convenience.                                                  | Can have tricky behavior in some contexts. ([docs.streamlit.io][2])  |

---

## Text Elements / Markup / Formatting

| Function                                       | Syntax                       | Purpose                                      | Notes / Gotchas                              |
| ---------------------------------------------- | ---------------------------- | -------------------------------------------- | -------------------------------------------- |
| `st.title(text)`                               | `st.title("...”)`            | Large page title.                            | Only one per page is common.                 |
| `st.header(text)`                              | `st.header("...”)`           | Major section header.                        | —                                            |
| `st.subheader(text)`                           | `st.subheader("...”)`        | Sub-section header.                          | —                                            |
| `st.markdown(text, unsafe_allow_html=False)`   | `st.markdown(...)`           | Markdown formatted text.                     | HTML possible if enabled.                    |
| `st.text(text)`                                | `st.text("…”)`               | Monospaced / preformatted plain text.        | No markup inside.                            |
| `st.latex(latex_string)`                       | `st.latex(r"…”)`             | Renders LaTeX math.                          | Needs valid LaTeX syntax.                    |
| `st.caption(text)`                             | `st.caption("…”)`            | Small, dim text caption.                     | Useful for minor notes.                      |
| `st.code(code_string, language="python")`      | `st.code("…", language="…”)` | Display code block with syntax highlighting. | Must pass proper language.                   |
| `with st.echo()`                               | `with st.echo(): …`          | Display the code inside block + run it.      | Good for tutorials / showing how code works. |
| `st.html(html_string, unsafe_allow_html=True)` | Renders raw HTML.            | Use carefully (security / styling concerns). |                                              |
| `st.help(object)`                              | `st.help(st.write)`          | Show docstring / help on object.             | Helpful for exploring.                       |
| `st.divider()`                                 | `st.divider()`               | Horizontal rule / separator.                 | Visual layout tool.                          |
| `st.badge(label)`                              | `st.badge("New")`            | Small colored badge.                         | Good to highlight new / statuses.            |

---

## Data Display Elements

| Function                                                                           | Syntax                         | Purpose                                                             | Notes / Gotchas                                   |
| ---------------------------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------- |
| `st.dataframe(data, width=None, height=None, use_container_width=False, **kwargs)` | Display interactive DataFrame. | Supports Pandas, Arrow etc.                                         | With/or without styling. ([docs.streamlit.io][4]) |
| `st.table(data)`                                                                   | `st.table(df or data)`         | Static table.                                                       | No interactive features like sort.                |
| `st.json(obj, expanded=False)`                                                     | Show JSON nicely.              | For nested dicts / JSON objects.                                    |                                                   |
| `st.metric(label, value, delta=None, delta_color="normal", help=None)`             | KPI + optional delta.          | Good for dashboards.                                                |                                                   |
| `st.data_editor(data, ...)`                                                        | Editable DataFrame widget.     | Allows user to edit data. (recently added) ([docs.streamlit.io][4]) |                                                   |

---

## Charts & Graphs / Visualization

| Function                                                      | Syntax                          | Purpose                                     | Notes / Gotchas |
| ------------------------------------------------------------- | ------------------------------- | ------------------------------------------- | --------------- |
| `st.line_chart(data, **kwargs)`                               | Quick line chart.               | Based on underlying data with minimal spec. |                 |
| `st.area_chart(data, **kwargs)`                               | Area under curve style.         | Good for totals over time.                  |                 |
| `st.bar_chart(data, **kwargs)`                                | Bar charts.                     | For categorical / distribution.             |                 |
| `st.map(data, **kwargs)`                                      | Map points by lat/lon.          | Data must have geographic coords.           |                 |
| `st.altair_chart(chart, use_container_width=False, **kwargs)` | Display Altair chart.           | More control.                               |                 |
| `st.plotly_chart(fig, **kwargs)`                              | Use Plotly figures.             | Highly interactive.                         |                 |
| `st.pydeck_chart(chart)`                                      | 3D / geospatial visualizations. | For richer maps / geography.                |                 |
| `st.graphviz_chart(data_or_dot, **kwargs)`                    | Graphviz network charts.        | Dependency on graphviz dot.                 |                 |
| `st.vega_lite_chart(data, spec, **kwargs)`                    | Vega-Lite charts.               | Declarative specification.                  |                 |
| `st.pyplot(fig, **kwargs)`                                    | Embed matplotlib figures.       | Classic plotting library.                   |                 |

---

## Input Widgets (All Types)

| Widget                                                                                                                                                                                                         | Syntax                                         | Returns / Behavior                | Notes / Gotchas |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------- | --------------- |
| `st.button(label, key=None, help=None, type=None, disabled=False)`                                                                                                                                             | Boolean (True only on click).                  | Click triggers one run.           |                 |
| `st.download_button(label, data, file_name=None, mime=None, key=None, help=None)`                                                                                                                              | Downloads file.                                | Data can be bytes, file path etc. |                 |
| `st.form_submit_button(label, **kwargs)`                                                                                                                                                                       | Submit button in a form (used with `st.form`). | Returns True when submitted.      |                 |
| `st.link_button(label, url, **kwargs)`                                                                                                                                                                         | Navigates to external URL.                     | Renders a link-like button.       |                 |
| `st.checkbox(label, value=False, key=None, help=None, disabled=False, label_visibility="visible")`                                                                                                             | True/False.                                    | Basic toggle.                     |                 |
| `st.color_picker(label, value=None, key=None, help=None, disabled=False, label_visibility="visible")`                                                                                                          | Color value (string or tuple).                 | Useful for theme / color choices. |                 |
| `st.radio(label, options, index=0, key=None, help=None, disabled=False, label_visibility="visible")`                                                                                                           | Single choice from list.                       | Returns selected.                 |                 |
| `st.selectbox(label, options, index=0, format_func=None, key=None, help=None, disabled=False, label_visibility="visible")`                                                                                     | Same as radio but dropdown.                    | Better for long lists.            |                 |
| `st.multiselect(label, options, default=None, key=None, help=None, disabled=False, label_visibility="visible")`                                                                                                | List of selections.                            | Returns list.                     |                 |
| `st.select_slider(label, options, value=None, key=None, help=None, disabled=False, label_visibility="visible")`                                                                                                | Select a value from list via slider.           | For discrete choices.             |                 |
| `st.slider(label, min_value, max_value, value=None, step=None, format=None, key=None, help=None, disabled=False, label_visibility="visible")`                                                                  | Numeric / date slider.                         | Use int/float or date/datetime.   |                 |
| `st.number_input(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, disabled=False, label_visibility="visible")`                                                  | Numeric (int/float) input.                     | Great for thresholds etc.         |                 |
| `st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")` | One-line text input.                           | Always returns string.            |                 |
| `st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, placeholder=None, disabled=False, label_visibility="visible")`                                                                | Multi-line text.                               | Useful for longer form input.     |                 |
| `st.date_input(label, value=None, min_value=None, max_value=None, key=None, help=None, disabled=False, label_visibility="visible")`                                                                            | Returns date object.                           | When selecting dates.             |                 |
| `st.time_input(label, value=None, key=None, help=None, disabled=False, label_visibility="visible")`                                                                                                            | Returns time object.                           | For times.                        |                 |
| `st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")`                                     | Uploaded file(s).                              | Returns file-like object(s).      |                 |
| `st.camera_input(label, key=None, help=None, disabled=False)`                                                                                                                                                  | Capture image from webcam.                     | Returns image object.             |                 |
| `st.toggle(label, value=False, key=None, help=None, disabled=False, label_visibility="visible")`                                                                                                               | True/False toggle switch.                      | UI preference.                    |                 |
| `st.feedback(label, ... )`                                                                                                                                                                                     | Rating / sentiment / feedback widget group.    | Returns some user feedback.       |                 |

---

## State, Caching & Execution Flow

| Concept / Function         | Syntax                                                  | What It Does                                | Notes / Gotchas                              |
| -------------------------- | ------------------------------------------------------- | ------------------------------------------- | -------------------------------------------- |
| `st.session_state`         | Use like `st.session_state["key"] = val`                | Store persistent variables between reruns.  | Must use unique keys; initialization needed. |
| `@st.cache_data`           | Decorate data-loading / pure functions                  | Cache result of functions returning data.   | Invalidate on code/data change or use `ttl`. |
| `@st.cache_resource`       | Decorate expensive resources (models, DB connections)   | Cache non-data objects.                     | Meant for singletons etc.                    |
| Conditional rerun triggers | Widgets with `on_change`, `key`, `args`, `kwargs`       | Widgets can trigger callbacks.              | Avoid circular callbacks.                    |
| `st.stop()`                | Stops the script execution (rest of script ignored).    | Useful for early exit on conditions.        |                                              |
| `st.experimental_rerun()`  | Force full script re-run.                               | Great for certain workflows; use carefully. |                                              |
| Multipage / Navigation     | Using `pages/` directory or `st.Page` / `st.navigation` | For structuring multi-page apps.            | Widget state across pages needs care.        |

---

## Layouts & Containers

| Concept / Function                                         | Syntax                                                 | Purpose                       | Notes / Gotchas                          |                      |
| ---------------------------------------------------------- | ------------------------------------------------------ | ----------------------------- | ---------------------------------------- | -------------------- |
| `st.sidebar`                                               | `st.sidebar.<widget/function>()` or `with st.sidebar:` | Widgets / display on sidebar. | For app settings etc.                    |                      |
| \`st.columns(n, \*, gap="small", vertical\_alignment="top" | "center"                                               | "bottom")\`                   | Returns column containers.               | Side-by-side layout. |
| `st.tabs(labels_list)`                                     | `tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])`             | Split content into tab views. | Only top-level; nested tabs have limits. |                      |
| `st.expander(label, *, expanded=False, icon=None)`         | Collapsible container.                                 | Good for optional detail.     |                                          |                      |
| `st.popover(label, *args, **kwargs)`                       | Popover UI container.                                  | For contextual UI.            |                                          |                      |
| `st.container()`                                           | Context manager; group arbitrary elements.             | Helps group logically.        |                                          |                      |
| `st.empty()`                                               | Placeholder container you can overwrite later.         | For dynamic UI updates.       |                                          |                      |

---

## Media & Assets

| Function                                                                                                               | Syntax                               | Accepts / Behavior   | Notes / Gotchas |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------------------- | --------------- |
| `st.image(image, caption=None, width=None, use_column_width=False, clamp=False, channels="RGB", output_format="auto")` | Images (file path, URL, NumPy, PIL). | Many format options. |                 |
| `st.audio(data, format=None)`                                                                                          | Audio data or file.                  | mp3, wav etc.        |                 |
| `st.video(data, format=None, start_time=0)`                                                                            | Video or URL or file-like.           | Large files may lag. |                 |
| `st.pdf(file or bytes, **kwargs)`                                                                                      | Display PDF inline.                  | Browser dependent.   |                 |

---

## Status / Feedback / Progress Indicators

| Function                                                              | Syntax                                | Purpose             | Notes / Gotchas        |
| --------------------------------------------------------------------- | ------------------------------------- | ------------------- | ---------------------- |
| `st.progress(int_percent)`                                            | `st.progress(50)`                     | Show progress bar.  | Percent from 0 to 100. |
| `with st.spinner(text): …`                                            | Show spinner while code runs.         | UI feedback.        |                        |
| `st.balloons()`                                                       | Show celebratory balloons.            | Only once; fun.     |                        |
| `st.success(msg)`, `st.error(msg)`, `st.warning(msg)`, `st.info(msg)` | Show messages styled by type.         | Visual feedback.    |                        |
| `st.exception(error_object, value=None, **kwargs)`                    | Show exception trace / error message. | Good for debugging. |                        |

---

## Configuration & Other Utilities

| Function / Concept                                                                                                                                                       | Syntax                                                                | Purpose                                              | Notes / Gotchas |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- | ---------------------------------------------------- | --------------- |
| `st.set_page_config(page_title=None, page_icon=None, layout="centered" or "wide", initial_sidebar_state="auto" or "expanded" or "collapsed", menu_items=None, **kwargs)` | Sets metadata, layout.                                                | Call early in script (before other st.\*).           |                 |
| `st.secrets["KEY"]`                                                                                                                                                      | Access secrets stored in `.streamlit/secrets.toml` or hosted secrets. | For credentials, API keys.                           |                 |
| `st.cache_data.clear()` / `st.cache_resource.clear()`                                                                                                                    | Clear caches manually.                                                | Useful during dev.                                   |                 |
| `st.experimental_memo` / `st.experimental_singleton` (older caching patterns)                                                                                            | Legacy cache patterns.                                                | Being phased or replaced.                            |                 |
| `st.theme` or theming options (via config)                                                                                                                               | Theming: color, fonts etc.                                            | Via `~/.streamlit/config.toml` or `set_page_config`. |                 |

---

## Paging, Navigation, Authentication & Context

| Function / Concept      | Syntax / Usage                                                                              | What It Enables                           | Notes / Gotchas                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------- |
| **Multipage Support**   | Use `pages/` directory (each script in pages become pages) or `st.navigation()` / `st.Page` | Build apps with multiple pages.           | State & widget behavior between pages needs careful keys. ([docs.streamlit.io][5]) |
| **Page Links**          | `st.page_link(target, label, icon=None)`                                                    | Link to other page in multi-page app.     | Nicely helps navigation. ([docs.streamlit.io][6])                                  |
| **Context / User Info** | `st.context` / `st.user` etc.                                                               | Get cookies, headers, locale, theme data. | Experimental / evolving. ([docs.streamlit.io][4])                                  |

---

## Miscellaneous / Advanced

| Concept / Function     | Behavior / Use Case                                                            | Notes / Gotchas                                               |
| ---------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Custom Components      | Use Streamlit Components to embed JS / React etc.                              | Requires building separate component.                         |
| Connections & DB       | Built-in connectors / ability to integrate external databases / snowflake etc. | Need to manage secrets, performance. ([docs.streamlit.io][3]) |
| App Testing Tools      | Tools to simulate / test apps programmatically.                                | Growing area.                                                 |
| Performance Monitoring | Options like profiling, caching, minimizing reruns.                            | Avoid expensive operations in global scope.                   |

---

## Beginner Pitfalls / Common Gotchas

* Forgetting to assign `key` on widgets when dynamic or multiple of same type
* Using `st.write()` too much — sometimes need more control with chart functions
* Not controlling layout early — e.g. using `set_page_config` after display calls doesn’t always work
* Cache invalidation issues — changing underlying data/code doesn’t always refresh cache as expected
* State not persisting across pages unless managed properly via `session_state`
* File upload / large media size causing slow load or memory issues

---

[1]: https://docs.streamlit.io/develop/api-reference/cli?utm_source=chatgpt.com "Command-line options - Streamlit Docs"
[2]: https://docs.streamlit.io/develop/api-reference/write-magic?utm_source=chatgpt.com "st.write and magic commands - Streamlit Docs"
[3]: https://docs.streamlit.io/develop/api-reference?utm_source=chatgpt.com "API Reference - Streamlit Docs"
[4]: https://docs.streamlit.io/develop/quick-reference/cheat-sheet?utm_source=chatgpt.com "Streamlit API cheat sheet"
[5]: https://docs.streamlit.io/develop/concepts/multipage-apps/widgets?utm_source=chatgpt.com "Working with widgets in multipage apps - Streamlit Docs"
[6]: https://docs.streamlit.io/develop/api-reference/widgets?utm_source=chatgpt.com "Input widgets - Streamlit Docs"
