import Link from "@docusaurus/Link";
import { motion } from "framer-motion";
import React from "react";
import { Badge } from "./ui/badge";
import { Card, CardContent, CardFooter, CardHeader } from "./ui/card";

interface Tool {
	name: string;
	description: string;
	tags: string[];
	link: string;
	image: string;
}

interface ToolCardProps {
	tool: Tool;
}

const ToolCard: React.FC<ToolCardProps> = ({ tool }) => {
	return (
		<motion.div
			whileHover={{ scale: 1.02 }}
			whileTap={{ scale: 0.98 }}
			className="transform transition-transform"
		>
			<Link to={tool.link} className="block">
				<Card className="relative overflow-hidden shadow-lg hover:shadow-xl transition-shadow rounded-lg">
					{/* Background Image with Gradient Overlay */}
					<div className="absolute inset-0">
						<img
							src={tool.image}
							alt={tool.name}
							className="w-full h-full object-cover"
						/>
						<div className="absolute inset-0 bg-gradient-to-t from-black via-transparent to-black opacity-70"></div>
					</div>
					{/* Content */}
					<div className="relative z-10 p-6 flex flex-col h-full">
						<CardHeader className="mb-2">
							<h3 className="text-2xl font-bold text-white drop-shadow-md">
								{tool.name}
							</h3>
						</CardHeader>
						<CardContent className="flex-grow">
							<p className="text-white mb-4">{tool.description}</p>
						</CardContent>
						<CardFooter>
							<div className="flex flex-wrap gap-2">
								{tool.tags.map((tag) => (
									<Badge
										key={tag}
										variant="outline"
										className="bg-white bg-opacity-30 text-white border-white hover:bg-white hover:text-gray-800 transition-colors"
									>
										{tag}
									</Badge>
								))}
							</div>
						</CardFooter>
					</div>
				</Card>
			</Link>
		</motion.div>
	);
};

export default ToolCard;
