# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "polars",
#     "altair",
#     "pyarrow",
#     "pandas",
# ]
# ///

import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import polars as pl
    import altair as alt
    return alt, mo, pl


@app.cell(hide_code=True)
def _(pl):
    # Pre-processed top 20 product codes data (from samd jan2025tojan2026.csv)
    data = [
        {"productcode": "QNP", "device_count": 4, "avg_days": 29, "min_days": 28, "max_days": 32},
        {"productcode": "QFM", "device_count": 3, "avg_days": 87, "min_days": 35, "max_days": 126},
        {"productcode": "QAS", "device_count": 14, "avg_days": 91, "min_days": 18, "max_days": 192},
        {"productcode": "POK", "device_count": 5, "avg_days": 106, "min_days": 25, "max_days": 158},
        {"productcode": "QJI", "device_count": 4, "avg_days": 130, "min_days": 68, "max_days": 249},
        {"productcode": "OMB", "device_count": 2, "avg_days": 135, "min_days": 126, "max_days": 143},
        {"productcode": "QHA", "device_count": 2, "avg_days": 145, "min_days": 119, "max_days": 170},
        {"productcode": "LLZ", "device_count": 13, "avg_days": 149, "min_days": 22, "max_days": 271},
        {"productcode": "OLZ", "device_count": 3, "avg_days": 153, "min_days": 90, "max_days": 254},
        {"productcode": "SDJ", "device_count": 2, "avg_days": 153, "min_days": 150, "max_days": 155},
        {"productcode": "QJU", "device_count": 2, "avg_days": 155, "min_days": 110, "max_days": 199},
        {"productcode": "QIH", "device_count": 75, "avg_days": 156, "min_days": 22, "max_days": 273},
        {"productcode": "QKB", "device_count": 6, "avg_days": 156, "min_days": 27, "max_days": 266},
        {"productcode": "QWO", "device_count": 2, "avg_days": 163, "min_days": 130, "max_days": 196},
        {"productcode": "JAK", "device_count": 5, "avg_days": 170, "min_days": 111, "max_days": 212},
        {"productcode": "QYE", "device_count": 3, "avg_days": 175, "min_days": 146, "max_days": 199},
        {"productcode": "QDQ", "device_count": 5, "avg_days": 200, "min_days": 54, "max_days": 279},
        {"productcode": "MYN", "device_count": 14, "avg_days": 207, "min_days": 103, "max_days": 282},
        {"productcode": "MUJ", "device_count": 6, "avg_days": 207, "min_days": 91, "max_days": 420},
        {"productcode": "OEB", "device_count": 3, "avg_days": 285, "min_days": 184, "max_days": 443},
    ]

    top20 = pl.DataFrame(data)
    top5_codes = top20.head(5)["productcode"].to_list()
    top20 = top20.with_columns(
        pl.when(pl.col("productcode").is_in(top5_codes))
        .then(pl.lit("Fastest (Top 5)"))
        .otherwise(pl.lit("Standard"))
        .alias("category")
    )
    return (top20,)


@app.cell
def _(mo):
    mo.md(
        """
        # Average FDA Clearance Time: Top 20 Product Codes
        **SaMD Devices | Jan 2025 - Jan 2026 | Sorted by average clearance time**
        """
    )
    return


@app.cell
def _(alt, top20):
    # Innolitics brand colors
    primary_color = "#2D3F86"
    highlight_color = "#E85036"

    base = alt.Chart(top20.to_pandas()).encode(
        y=alt.Y(
            "productcode:N",
            sort=alt.EncodingSortField(field="avg_days", order="ascending"),
            title=None,
            axis=alt.Axis(labelFontSize=13, labelFont="system-ui")
        ),
    )

    lines = base.mark_rule(strokeWidth=2, opacity=0.6).encode(
        x=alt.X("avg_days:Q", title="Average Days to Clearance"),
        x2=alt.value(0),
        color=alt.Color(
            "category:N",
            scale=alt.Scale(
                domain=["Fastest (Top 5)", "Standard"],
                range=[highlight_color, primary_color]
            ),
            legend=alt.Legend(title=None, orient="bottom", direction="horizontal")
        ),
    )

    points = base.mark_circle(size=200, opacity=1).encode(
        x=alt.X("avg_days:Q"),
        color=alt.Color("category:N"),
        tooltip=[
            alt.Tooltip("productcode:N", title="Product Code"),
            alt.Tooltip("avg_days:Q", title="Avg Days"),
            alt.Tooltip("device_count:Q", title="Device Count"),
            alt.Tooltip("min_days:Q", title="Min Days"),
            alt.Tooltip("max_days:Q", title="Max Days"),
        ]
    )

    labels = base.mark_text(
        align="left", dx=14, fontSize=11, color="#666666", font="system-ui"
    ).encode(
        x=alt.X("avg_days:Q"),
        text=alt.Text("label:N"),
    ).transform_calculate(
        label="datum.avg_days + 'd (n=' + datum.device_count + ')'"
    )

    chart = (lines + points + labels).properties(
        width=700,
        height=500,
    ).configure_view(
        strokeWidth=0
    ).configure_axis(
        grid=True,
        gridColor="#E0E0E0",
        gridDash=[3, 3],
        domainColor="#E0E0E0",
    )

    chart
    return


@app.cell
def _(mo, top20):
    fastest = top20.head(1)
    slowest = top20.tail(1)

    mo.md(
        f"""
        ---
        **Key Insights:**
        - **Fastest:** {fastest["productcode"][0]} at {fastest["avg_days"][0]} days (n={fastest["device_count"][0]})
        - **Slowest:** {slowest["productcode"][0]} at {slowest["avg_days"][0]} days (n={slowest["device_count"][0]})
        - **Total devices in top 20:** {top20["device_count"].sum()}
        """
    )
    return


@app.cell
def _(mo):
    logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="120" height="30" viewBox="0 0 175 43" fill="none"><g clip-path="url(#a)"><path fill="url(#b)" d="M0 21.55v8.213c0 .873.225 1.731.652 2.487a4.919 4.919 0 0 0 1.78 1.82l6.993 4.132.044.025 9.408-5.558-9.452-5.582-9.399-5.552-.026.016Z"/><path fill="url(#c)" d="m28.273 4.847-9.382 5.543 9.382 5.542v.02l9.426 5.566V13.24c0-.874-.225-1.732-.652-2.488a4.92 4.92 0 0 0-1.78-1.822l-6.951-4.108-.043.025Z"/><path fill="url(#d)" d="m28.273 38.204 6.994-4.131a4.918 4.918 0 0 0 1.78-1.82 5.062 5.062 0 0 0 .652-2.488v-8.247l-9.426-5.567v22.253Z"/><path fill="url(#e)" d="m18.878 32.669-9.41 5.558 6.952 4.106c.74.437 1.578.667 2.432.667.854 0 1.692-.23 2.432-.667l6.976-4.121.015-.01V27.118L18.88 32.67Z"/><path fill="url(#f)" d="M2.432 8.929a4.92 4.92 0 0 0-1.78 1.82A5.064 5.064 0 0 0 0 13.239v8.278l.026.016 9.399 5.552V4.816l-.016-.01L2.432 8.93Z"/><path fill="url(#g)" d="M18.824 0a4.777 4.777 0 0 0-2.405.664L9.426 4.797v11.135l9.41-5.558.015-.009.043.025 9.382-5.543v-.05L21.282.667A4.777 4.777 0 0 0 18.878 0h-.054Z"/><path fill="#2D3F86" d="M51.782 10.917v19.797h-5.407V10.917h5.407ZM64.71 14.82c1.783 0 3.2.609 4.248 1.826 1.048 1.198 1.572 2.826 1.572 4.886v9.182h-5.407v-8.452c0-.899-.23-1.6-.69-2.106-.46-.524-1.076-.787-1.848-.787-.81 0-1.444.263-1.903.787-.46.505-.69 1.207-.69 2.106v8.452h-5.407V14.961h5.407v2.246c.478-.711 1.122-1.282 1.931-1.713.81-.449 1.738-.674 2.786-.674ZM83.345 14.82c1.784 0 3.2.609 4.248 1.826 1.049 1.198 1.573 2.826 1.573 4.886v9.182h-5.407v-8.452c0-.899-.23-1.6-.69-2.106-.46-.524-1.076-.787-1.848-.787-.81 0-1.444.263-1.904.787-.46.505-.69 1.207-.69 2.106v8.452h-5.406V14.961h5.407v2.246c.478-.711 1.122-1.282 1.93-1.713.81-.449 1.739-.674 2.787-.674ZM99.057 30.91c-1.545 0-2.934-.327-4.166-.982a7.198 7.198 0 0 1-2.869-2.808c-.699-1.217-1.048-2.65-1.048-4.297 0-1.628.35-3.051 1.048-4.268a7.385 7.385 0 0 1 2.897-2.808c1.232-.655 2.62-.983 4.165-.983s2.924.328 4.138.983a7.154 7.154 0 0 1 2.897 2.808c.717 1.217 1.076 2.64 1.076 4.268 0 1.63-.359 3.061-1.076 4.297a7.154 7.154 0 0 1-2.897 2.808c-1.232.655-2.62.983-4.165.983Zm0-4.773c.754 0 1.379-.28 1.876-.842.514-.58.772-1.404.772-2.472 0-1.067-.258-1.88-.772-2.443-.497-.561-1.113-.842-1.849-.842-.735 0-1.352.28-1.848.842-.497.562-.745 1.376-.745 2.444 0 1.085.24 1.909.717 2.47.479.562 1.095.843 1.849.843ZM114.525 9.934v20.78h-5.406V9.934h5.406ZM120.06 13.5c-.957 0-1.729-.262-2.318-.786-.57-.543-.855-1.217-.855-2.022 0-.823.285-1.507.855-2.05.589-.542 1.361-.814 2.318-.814.938 0 1.692.272 2.262.814.588.543.883 1.227.883 2.05 0 .805-.295 1.48-.883 2.022-.57.524-1.324.787-2.262.787Zm2.676 1.46v15.754h-5.407V14.961h5.407ZM134.67 26.025v4.69h-2.345c-3.954 0-5.931-1.994-5.931-5.982v-5.195h-1.903v-4.577h1.903v-3.82h5.434v3.82h2.814v4.577h-2.814v5.28c0 .43.092.739.276.926.203.187.534.28.993.28h1.573ZM139.605 13.5c-.956 0-1.729-.262-2.317-.786-.57-.543-.855-1.217-.855-2.022 0-.823.285-1.507.855-2.05.588-.542 1.361-.814 2.317-.814.938 0 1.692.272 2.262.814.589.543.883 1.227.883 2.05 0 .805-.294 1.48-.883 2.022-.57.524-1.324.787-2.262.787Zm2.676 1.46v15.754h-5.407V14.961h5.407ZM144.201 22.823c0-1.628.331-3.051.993-4.268.662-1.217 1.582-2.153 2.759-2.808 1.195-.655 2.556-.983 4.083-.983 1.968 0 3.623.553 4.965 1.657 1.343 1.086 2.207 2.611 2.593 4.577h-5.738c-.331-1.03-.974-1.544-1.931-1.544-.68 0-1.223.29-1.627.87-.386.562-.579 1.395-.579 2.5 0 1.104.193 1.946.579 2.527.404.58.947.87 1.627.87.975 0 1.619-.515 1.931-1.544h5.738c-.386 1.947-1.25 3.473-2.593 4.577-1.342 1.105-2.997 1.657-4.965 1.657-1.527 0-2.888-.328-4.083-.983-1.177-.655-2.097-1.591-2.759-2.808-.662-1.217-.993-2.65-.993-4.297ZM168.158 30.91c-1.398 0-2.649-.233-3.752-.701-1.085-.487-1.949-1.142-2.593-1.966a5.283 5.283 0 0 1-1.048-2.836h5.241c.074.505.303.899.69 1.18.386.28.864.42 1.434.42.442 0 .791-.093 1.048-.28.258-.187.387-.43.387-.73 0-.393-.212-.684-.635-.87-.423-.188-1.122-.394-2.096-.619-1.104-.224-2.023-.477-2.759-.758a4.8 4.8 0 0 1-1.931-1.376c-.533-.636-.8-1.497-.8-2.583 0-.936.248-1.779.745-2.528.496-.767 1.223-1.376 2.179-1.825.975-.45 2.143-.674 3.504-.674 2.023 0 3.613.506 4.772 1.517 1.159 1.01 1.83 2.34 2.014 3.987h-4.883c-.092-.505-.313-.89-.662-1.151-.331-.281-.782-.421-1.352-.421-.441 0-.781.084-1.02.252-.221.169-.332.403-.332.702 0 .375.212.665.635.87.423.188 1.103.385 2.041.59 1.122.244 2.051.515 2.787.815.754.3 1.406.786 1.958 1.46.57.655.855 1.554.855 2.696 0 .917-.266 1.741-.8 2.471-.515.73-1.259 1.31-2.234 1.741-.956.412-2.088.618-3.393.618Z"/></g><defs><linearGradient id="b" x1="4.398" x2="12.528" y1="18.614" y2="36.196" gradientUnits="userSpaceOnUse"><stop stop-color="#2D3F86" stop-opacity=".404"/><stop offset="1" stop-color="#2D3F86"/></linearGradient><linearGradient id="c" x1="33.335" x2="25.242" y1="24.69" y2="6.909" gradientUnits="userSpaceOnUse"><stop stop-color="#2D3F86" stop-opacity=".396"/><stop offset="1" stop-color="#2D3F86"/></linearGradient><linearGradient id="d" x1="23.438" x2="37.011" y1="35.757" y2="31.432" gradientUnits="userSpaceOnUse"><stop stop-color="#2D3F86" stop-opacity=".396"/><stop offset="1" stop-color="#2D3F86"/></linearGradient><linearGradient id="e" x1="9.243" x2="28.274" y1="32.613" y2="32.88" gradientUnits="userSpaceOnUse"><stop stop-color="#2D3F86" stop-opacity=".404"/><stop offset="1" stop-color="#2D3F86"/></linearGradient><linearGradient id="f" x1="14.722" x2=".498" y1="6.5" y2="11.021" gradientUnits="userSpaceOnUse"><stop stop-color="#2D3F86" stop-opacity=".404"/><stop offset="1" stop-color="#2D3F86"/></linearGradient><linearGradient id="g" x1="28.276" x2="9.426" y1="10.308" y2="10.197" gradientUnits="userSpaceOnUse"><stop stop-color="#2D3F86" stop-opacity=".396"/><stop offset="1" stop-color="#2D3F86"/></linearGradient><clipPath id="a"><path fill="#fff" d="M0 0h175v43H0z"/></clipPath></defs></svg>'''

    mo.md(
        f"""
        <div style="text-align: right; opacity: 0.6; margin-top: 20px;">
            {logo_svg}
        </div>
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ---
        ## Data Processing Code

        The visualization above was created from FDA 510(k) clearance data for SaMD devices.
        Below is how the data was processed:
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ```python
        import polars as pl

        # Load raw FDA clearance data
        df = pl.read_csv("samd jan2025tojan2026.csv")

        # Get top 20 product codes by clearance volume
        top20 = (
            df.filter(
                (pl.col("productcode").is_not_null()) &
                (pl.col("productcode") != "") &
                (pl.col("days_to_clearance").is_not_null())
            )
            .group_by("productcode")
            .agg([
                pl.count().alias("device_count"),
                pl.col("days_to_clearance").mean().round(0).alias("avg_days"),
                pl.col("days_to_clearance").min().alias("min_days"),
                pl.col("days_to_clearance").max().alias("max_days"),
            ])
            .sort("device_count", descending=True)
            .head(20)
            .sort("avg_days")  # Sort by clearance time for visualization
        )
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ### Dataset Summary
        - **Source:** FDA 510(k) clearance database
        - **Period:** January 2025 - January 2026
        - **Filter:** Software as a Medical Device (SaMD) only
        - **Total records:** 206 clearances across 46 product codes
        """
    )
    return


if __name__ == "__main__":
    app.run()
