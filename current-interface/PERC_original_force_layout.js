      var svg = d3.select("svg"),
          width = +svg.attr("width"),
          height = +svg.attr("height");

      var radius = 5;
      var color = d3.scaleOrdinal(d3.schemeCategory20);

    // for circle packing
     /* var pack = d3.pack()
        .size([width - 2, height - 2])
        .padding(3);*/

// this sounds good idea ; to create hierachy
/*      var stratify = d3.stratify()
        .id(function(d) { return d.id; })
        .parentId(function(d) { return d.group; });*/

      d3.json("10000.json", function(error, graph) {
        if (error) throw error;

      var simulation = d3.forceSimulation()
          .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(30))
          .force("charge", d3.forceManyBody().strength(-2))
          .force("center", d3.forceCenter(width / 2, height / 2));

      var link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
          .attr("stroke-width", function(d) { return Math.sqrt(Math.sqrt(Math.sqrt(d.value))); });

      var node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph.nodes)
        .enter().append("circle")
          .attr("r", radius)
          .attr("fill", function(d) { return color(d.group); });

      node.append("title")
        .text(function(d) { return d.id; });

      simulation
          .nodes(graph.nodes)
          .on("tick", ticked);

      simulation.force("link")
          .links(graph.links);

      function ticked() {
        link
            .attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node
            .attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; });
      }

/*      var root = stratify(graph)
          .sum(function(d) { return d.value; })
          .sort(function(a, b) { return b.value - a.value; });

      var root = d3.hierarchy({children: classes})
            .sum(function(d) { return d.value; })
            .each(function(d) {
              if (id = d.data.id) {
                var id, i = id.lastIndexOf(".");
                d.id = id;
                d.package = id.slice(0, i);
                d.class = id.slice(i + 1);
              }
            });

      var entries = d3.nest()
          .key(function(d) { return d.group; })
          .map(graph);

      pack(entries);

        var packNode = svg
    .selectAll("g")
    .data(root.descendants())
    .enter().append("g")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
      .attr("class", function(d) { return "node" + (!d.children ? " node--leaf" : d.depth ? "" : " node--root"); })
      .each(function(d) { d.node = this; })
      .on("mouseover", hovered(true))
      .on("mouseout", hovered(false));

  packNode.append("circle")
      .attr("id", function(d) { return "node-" + d.id; })
      .attr("r", function(d) { return d.r; })
      .style("fill", function(d) { return color(d.depth); });
*/
    });


/*function hovered(hover) {
  return function(d) {
    d3.selectAll(d.ancestors().map(function(d) { return d.node; })).classed("node--hover", hover);
  }; */