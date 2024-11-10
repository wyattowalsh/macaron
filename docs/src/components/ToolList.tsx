import { motion } from "framer-motion";
import React, { useMemo, useState } from "react";
import tools from "../constants/toolsData";
import ToolCard from "./ToolCard";
import { Input } from "./ui/input";
import { Select, SelectContent, SelectItem, SelectTrigger } from "./ui/select";
import { Badge } from "./ui/badge";

interface ToolListProps {
	tag?: string;
}

const ToolList: React.FC<ToolListProps> = ({ tag }) => {
	const [searchTerm, setSearchTerm] = useState<string>("");
	const [selectedTags, setSelectedTags] = useState<string[]>(tag ? [tag] : []);
	const [sortOption, setSortOption] = useState<"name" | "tags">("name");

	const allTags = useMemo(
		() => Array.from(new Set(tools.flatMap((tool) => tool.tags))).sort(),
		[]
	);

	const filteredTools = useMemo(() => {
		return tools
			.filter(
				(tool) =>
					tool.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
					tool.description.toLowerCase().includes(searchTerm.toLowerCase())
			)
			.filter(
				(tool) =>
					selectedTags.length === 0 ||
					selectedTags.every((tag) => tool.tags.includes(tag))
			)
			.sort((a, b) => {
				if (sortOption === "name") {
					return a.name.localeCompare(b.name);
				} else if (sortOption === "tags") {
					return a.tags[0]?.localeCompare(b.tags[0]) || 0;
				}
				return 0;
			});
	}, [searchTerm, selectedTags, sortOption]);

	const toggleTag = (tag: string) => {
		setSelectedTags((prevSelectedTags) =>
			prevSelectedTags.includes(tag)
				? prevSelectedTags.filter((t) => t !== tag)
				: [...prevSelectedTags, tag]
		);
	};

	return (
		<div className="container mx-auto px-4">
			{/* Search and Sort Section */}
			<div className="flex flex-col md:flex-row md:items-center md:justify-between mb-6 space-y-4 md:space-y-0">
				<div className="relative w-full md:w-1/2">
					<label htmlFor="tool-search" className="sr-only">
						Search tools
					</label>
					<Input
						id="tool-search"
						type="text"
						placeholder="Search tools..."
						value={searchTerm}
						onChange={(e) => setSearchTerm(e.target.value)}
						className="pl-10"
					/>
					<svg
						className="absolute left-3 top-2.5 text-gray-500 w-5 h-5"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
						aria-hidden="true"
					>
						<path
							strokeLinecap="round"
							strokeLinejoin="round"
							strokeWidth="2"
							d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
						/>
					</svg>
				</div>
				<div className="w-full md:w-48">
					<label htmlFor="sort-options" className="sr-only">
						Sort options
					</label>
					<Select
						id="sort-options"
						value={sortOption}
						onValueChange={(value) => setSortOption(value as "name" | "tags")}
					>
						<SelectTrigger>{`Sort by ${
							sortOption === "name" ? "Name" : "Tags"
						}`}</SelectTrigger>
						<SelectContent>
							<SelectItem value="name">Sort by Name</SelectItem>
							<SelectItem value="tags">Sort by Tags</SelectItem>
						</SelectContent>
					</Select>
				</div>
			</div>

			{/* Tags Filter Section */}
			<div className="mb-6 flex flex-wrap gap-2">
				{allTags.map((tagItem) => {
					const isSelected = selectedTags.includes(tagItem);
					return (
						<motion.button
							key={tagItem}
							whileHover={{ scale: 1.05 }}
							whileTap={{ scale: 0.95 }}
							className={`cursor-pointer px-3 py-1 rounded-full transition duration-200 ease-in-out transform ${
								isSelected
									? "bg-gradient-to-r from-purple-500 to-indigo-500 text-white shadow-lg"
									: "bg-white text-gray-800 border border-gray-300 hover:bg-gray-100"
							}`}
							onClick={() => toggleTag(tagItem)}
							aria-pressed={isSelected}
						>
							{tagItem}
						</motion.button>
					);
				})}
			</div>

			{/* Tools Grid Section */}
			<motion.div
				layout
				className="grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3"
			>
				{filteredTools.map((tool) => (
					<ToolCard key={tool.link} tool={tool} />
				))}
			</motion.div>
		</div>
	);
};

export default ToolList;
